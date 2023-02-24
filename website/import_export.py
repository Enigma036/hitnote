from flask import Blueprint, render_template, send_file, redirect, url_for, jsonify, request
from flask import make_response
from flask_login import login_required, current_user
from datetime import datetime
from .models import Note, User
from website import create_first_user
from .sort_and_filtration import filtrateNotes, getFormData, getSortData, sort_items
from . import db
from sqlalchemy import desc
import os
import csv
import io
import uuid



import_export = Blueprint("import_export", __name__) 

@import_export.route("/importexport", methods=["GET","POST"])
@login_required
def page():
    
    error_message1 = "Zprava"
    trida1 = "none"
    error_message2 = "Zprava"
    trida2 = "none"
    
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

                error_message1 = "Soubor úspěšně importován"
                trida1 = "success"

                with open(input.filename, 'r', newline="") as csv_file:
                    reader = csv.reader(csv_file)

                    for row in reader:
                        try:
                            ajdy = row[0]
                            datum = datetime.strptime(row[1], '%Y-%m-%d').date()
                            cas = row[2]
                            jazyk = row[3]
                            hodnoceni = row[4]
                            text = row[5]
                            print(Note.query.filter_by(id=ajdy).all())
                            if Note.query.filter_by(id=ajdy).all() == []:
                                new_note = Note(id = ajdy, date = datum, language = jazyk, interval = cas, stars = hodnoceni, user_id = current_user.id, data = text)
                            else:
                                new_note = Note(id=str(uuid.uuid4()), date = datum, language = jazyk, interval = cas, stars = hodnoceni, user_id = current_user.id, data = text)
                                error_message1 = "Aby nedošlo ke kolizi, muselo být id alespoň jedné zprávy změněno"
                                trida1 = "error"
                            db.session.add(new_note)
                            db.session.commit()
                        except:
                            error_message1 = "Nepodařilo se importovat některé zprávy"
                            trida1 = "error"
                os.remove(input.filename)
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
                notes = Note.query.filter_by(user_id=current_user.id).all()
                output = io.StringIO()
                writer = csv.writer(output)

                for note in notes:
                    writer.writerow([note.id, note.date, note.interval, note.language, note.stars, note.data])
                error_message2 = "Soubor úspěšně exportován"
                trida2 = "succes"
            except:
                error_message2 = "Nastala chyba při exportování souboru"
                trida2 = "error"

            # Vytvoření odpovědi pro stahování souboru
            response = make_response(output.getvalue())
            response.headers["Content-Disposition"] = "attachment; filename=notes.csv"
            response.headers["Content-type"] = "text/csv"

            return response
    
    return render_template("import_export.html", programmer = current_user, message_import = error_message1, message_export = error_message2, trida1 = trida1, trida2 = trida2)