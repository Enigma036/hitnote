from flask import Blueprint, render_template, redirect, url_for, jsonify, request
from datetime import datetime
from .models import Note, User
from website import create_first_user
from .sort_and_filtration import filtrateNotes, getFormData, getSortData, sort_items
from . import db
from sqlalchemy import desc



views = Blueprint("views", __name__) 

@views.route("/")
def home():
    create_first_user()
    return redirect(url_for("views.main_window", user=1))
    
@views.route("/<user>", methods=["GET","POST"])
def main_window(user):
    create_first_user()
    
    notes = User.query.filter_by(id=user).first_or_404().notes
    unique_languages = []
    
    if notes:
        for note in notes:
            if note.language not in unique_languages:
                unique_languages.append(note.language)
    else:
        unique_languages.append("Žádný jazyk") 
    
    if request.method == 'POST':
        ScriptFunction = ""
        
        IsChecked, date1, date2, interval1, interval2, language1, stars1, stars2  = getFormData(request)
        if IsChecked:
            notes = filtrateNotes(notes, user, date1, date2, interval1, interval2, language1, stars1, stars2)

        if(request.form.get("dateTH") == "↑" or request.form.get("dateTH") == "↕"  or request.form.get("dateTH") == "↓"):
            orderList, dateS, languageS, intervalS, starsS = getSortData(request)
            notes = sort_items(notes, user, dateS, languageS, intervalS, starsS, orderList)
    
    if request.method == 'GET':
        ScriptFunction =  'loadActiveFormAfterLoad("FormFiltration1");'

    return render_template("main.html", programmers=User.query.all(), user_id = int(user), notes = notes, unique_languages = unique_languages, ScriptFunction=ScriptFunction)
