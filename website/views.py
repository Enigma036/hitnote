from flask import Blueprint, render_template, redirect, url_for, jsonify, request
from flask_login import login_required, current_user
from datetime import datetime
from .models import Note, User
from website import create_first_user
from .sort_and_filtration import filtrateNotes, getFormData, getSortData, sort_items
from . import db
from sqlalchemy import desc



views = Blueprint("views", __name__) 

@views.route("/", methods=['GET', 'POST'])
@login_required
def home():
    create_first_user()
    
    notes = User.query.filter_by(id=current_user.id).first_or_404().notes
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
            notes = filtrateNotes(notes, current_user.id, date1, date2, interval1, interval2, language1, stars1, stars2)

        if(request.form.get("dateTH") == "↑" or request.form.get("dateTH") == "↕"  or request.form.get("dateTH") == "↓"):
            orderList, dateS, languageS, intervalS, starsS = getSortData(request)
            notes = sort_items(notes, current_user.id, dateS, languageS, intervalS, starsS, orderList)
    
    if request.method == 'GET':
        ScriptFunction =  'loadActiveFormAfterLoad("FormFiltration1");'

    return render_template("main.html", programmer= current_user, user_id = int(current_user.id), notes = notes, unique_languages = unique_languages, ScriptFunction=ScriptFunction)
