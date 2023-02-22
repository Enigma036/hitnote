from flask import Blueprint, render_template, redirect, url_for, jsonify, request
from flask_login import login_required, current_user
from datetime import datetime
from .models import Note, User
from website import create_first_user
from .sort_and_filtration import filtrateNotes, getFormData, getSortData, sort_items
from . import db
from sqlalchemy import desc
import os
import csv
import sqlite3



import_export = Blueprint("import_export", __name__) 

@import_export.route("/importexport", methods=["GET","POST"])
@login_required
def page():
    
    error_messages = "Zprava"
    trida = "none"
    
    if request.method == "POST":
        import_export_messsage = request.form.get('ImportExportMessage')
        
        # Když zmáčkne na tlačítko import
        if import_export_messsage == "IMPORT":
            input = request.files["input_file"]
            input.save(input.filename)

            with open(input.filename, 'r', newline="") as csv_file:
                reader = csv.reader(csv_file)

                for row in reader:
                    try:
                        datum = datetime.strptime(row[1], '%Y-%m-%d').date()
                        cas = row[2]
                        jazyk = row[3]
                        hodnoceni = row[4]
                        text = row[5]
                        new_note = Note(date = datum, language = jazyk, interval = cas, stars = hodnoceni, user_id = current_user.id, data = text)
                        db.session.add(new_note)
                        db.session.commit()
                    except:
                        error_messages = "Nepodařilo se importovat některé zprávy"
                        trida = "error"
            os.remove(input.filename)
        
        # Když zmáčkne na tlačítko export
        elif import_export_messsage == "EXPORT":
            db_name = 'database.db'
            table_name = 'note'
            output_file = 'output.csv'
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM " + table_name)
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            with open(output_file, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                for row in rows:
                    row_list = list(row)
                    if row_list[5] == current_user.id:
                        row_list[2], row_list[3] = row_list[3], row_list[2]
                        del row_list[5]
                        row_list[5] = row_list[5].replace("\r", "\\r").replace("\n", "\\n").strip()
                        writer.writerow(row_list)
    
    return render_template("import_export.html", programmer = current_user, message = error_messages, trida = trida)