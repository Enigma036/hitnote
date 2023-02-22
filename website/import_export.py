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
import sqlite3
import io



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
            notes = Note.query.filter_by(user_id=current_user.id).all()
            output = io.StringIO()
            writer = csv.writer(output)

            for note in notes:
                writer.writerow([note.id, note.date, note.interval, note.language, note.stars, note.data])

            # Vytvoření odpovědi pro stahování souboru
            response = make_response(output.getvalue())
            response.headers["Content-Disposition"] = "attachment; filename=notes.csv"
            response.headers["Content-type"] = "text/csv"

            return response
    
    return render_template("import_export.html", programmer = current_user, message = error_messages, trida = trida)