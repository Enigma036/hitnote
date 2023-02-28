
from flask import Blueprint, render_template, send_file, redirect, url_for, jsonify, request
from flask import make_response
from flask_login import login_required, current_user
from datetime import datetime, date
from .models import Note, User
from website import create_first_user
from .sort_and_filtration import filtrateNotes, getFormData, getSortData, sort_items
from . import db
from sqlalchemy import desc
import os
import csv
import io
import sqlite3
import uuid



import_export = Blueprint("import_export", __name__) 

@import_export.route("/importexport", methods=["GET","POST"])
@login_required
def page():
    
    error_message1 = "Zprava"
    trida1 = "none"
    error_message2 = "Zprava"
    trida2 = "none"
    
    message = []
    
    pocet_importovanych = 0
    pocet_spatnych = 0
    pocet_zmenenych = 0
    
    if request.method == "POST":
        import_export_messsage = request.form.get('ImportExportMessage')
        
        # Když zmáčkne na tlačítko import
        if import_export_messsage == "IMPORT":
            try:
                notes = Note.query.filter_by(user_id=current_user.id).all()
                for note in notes:
                    db.session.delete(note)
            except:
                    error_message1 = "Nepodařilo se smazat stávající záznamy"
                    trida1 = "error"

            try:
                input = request.files["input_file"]
                input.save(input.filename)

                error_message1 = "Soubor byl úspěšně importován"
                trida1 = "success"

                with open(input.filename, 'r', newline="", encoding="utf-8-sig") as csv_file:
                    reader = csv.reader(csv_file, delimiter=';')
                    header = next(csv_file)
                    for row in reader:
                        try:
                            ajdy = row[0]
                            try:
                                datum = datetime.strptime(row[1], '%d-%m-%Y').date()
                            except:
                                datum = datetime.strptime(row[1], '%d.%m.%Y').date()
                            cas = row[2]
                            jazyk = row[3]
                            hodnoceni = row[4]
                            text = row[5]
                            
                            text = text.replace("\\r", "\r").replace("\\n","\n")

                            try:
                                datetime(year=int(datum.year),month=int(datum.month),day=int(datum.day))
                            
                            except:
                                pocet_spatnych += 1
                                
                            if jazyk == None or jazyk.isspace() or len(jazyk) < 1 or len(jazyk) > 30:
                                pocet_spatnych += 1

                            elif cas == None or cas=="" or int(cas) < 1 or int(cas) > 1440:
                                pocet_spatnych += 1
                                
                            elif hodnoceni == "" or int(hodnoceni) > 5 or int(hodnoceni) < 0:
                                pocet_spatnych += 1
                            
                            elif text == None or len(text) < 1 or len(text) > 300 or text.isspace():
                                pocet_spatnych += 1

                            else:
                            
                                if Note.query.filter_by(id=ajdy).all() == []:
                                    new_note = Note(id = ajdy, date = datum, language = jazyk, interval = cas, stars = hodnoceni, user_id = current_user.id, data = text)
                                    pocet_importovanych += 1
                                else:
                                    new_note = Note(id=str(uuid.uuid4()), date = datum, language = jazyk, interval = cas, stars = hodnoceni, user_id = current_user.id, data = text)
                                    error_message1 = "Aby nedošlo ke kolizi, muselo být ID alespoň jedné zprávy změněno"
                                    trida1 = "error"
                                    pocet_zmenenych += 1
                                
                                db.session.add(new_note)
                                db.session.commit()
                            
                        except:
                            pocet_spatnych += 1
                
                os.remove(input.filename)
                
                
                if pocet_importovanych and not pocet_zmenenych and not pocet_spatnych:
                    error_message1 = "Soubor byl úspěšně importován"
                    trida1 = "success"
                else:
                    trida1 = "error"
                    if pocet_importovanych:
                        message.append(f"Bylo importováno {pocet_importovanych} záznam/ů")
                    if pocet_zmenenych:
                        message.append(f"U {pocet_zmenenych} záznamu/ů bylo změněno ID")
                    if pocet_spatnych:
                        message.append(f"{pocet_spatnych} záznam/ů nebyl/o importováno")
                
                if message:
                    for i in range(len(message)):
                        if i == 0:
                            error_message1 = message[i]
                        else:
                            error_message1 += "<br>" + message[i]
                            
            except:
                error_message1 = "Nepodařilo se nahrát soubor"
                trida1 = "error"
                try:
                    for note in notes:
                        db.session.add(note)
                except:
                    error_message1 = "Nepodařilo se nahrát zálohované zprávy"
                    trida1 = "error"
                    
        # Když zmáčkne na tlačítko export
        elif import_export_messsage == "EXPORT":
            try:
                db_name = "instance/database.db"
                table_name = 'note'
                output_file = current_user.username + "-" + str(date.today()) + ".csv"
                conn = sqlite3.connect(db_name)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM " + table_name)
                rows = cursor.fetchall()
                cursor.close()
                conn.close()
                
                with open(output_file, 'w', newline='', encoding='utf-8-sig') as csv_file:
                    writer = csv.writer(csv_file, delimiter=';')
                    for row in rows:
                        header = list(row)
                        header[0], header[1], header[2], header[3], header[4], header[5], header[6] = "id", "date", "time-spent", "programming-language", "rating", "description", ""
                        writer.writerow(header)
                        break
                    for row in rows:
                        row_list = list(row)
                        if row_list[5] == current_user.id:
                            row_list[1] = datetime.strptime(row_list[1], '%Y-%m-%d')
                            row_list[1] = row_list[1].strftime('%d-%m-%Y')
                            row_list[2], row_list[3] = row_list[3], row_list[2]
                            del row_list[5]
                            row_list[5] = row_list[5].replace("\r", "\\r").replace("\n", "\\n").strip()
                            writer.writerow(row_list)

                csv_file.close()
                
                output_file = "../" + output_file
                response = send_file(output_file, as_attachment=True)

                return response
        
            except:
                error_message2 = "Nastala chyba při exportování souboru"
                trida2 = "error"
    
    try:
        folder_path = os.getcwd()
        for file_name in os.listdir(folder_path):
            print(file_name)
            if file_name.endswith(".csv") and file_name.startswith(str(current_user.username)):
                os.remove(os.path.join(folder_path, file_name))
    except:
        pass
        

    
    return render_template("import_export.html", programmer = current_user, message_import = error_message1, message_export = error_message2, trida1 = trida1, trida2 = trida2)