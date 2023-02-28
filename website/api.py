from flask import Blueprint, render_template, redirect, url_for, jsonify, Response, request, abort
from flask_login import login_required, current_user
from datetime import datetime
from .models import Note, User
from website import create_first_user
from .sort_and_filtration import filtrateNotes, getFormData, getSortData, sort_items
from . import db
from sqlalchemy import desc
import json
import uuid


# Dodělat filtraci

api = Blueprint("api", __name__) 

@api.route("/users/<string:user_id>/records/<string:record_id>",  methods=['GET', 'PUT','DELETE'])
def record(user_id, record_id):
    
    if request.method == "PUT":
        note = Note.query.filter_by(id=record_id, user_id=user_id).first()
        if note:
            if True:
                data = request.get_json()
                
                new_id = (data["id"])
                new_date = datetime.strptime(data["date"], '%Y-%m-%d').date()
                new_interval = int(data["time_spent"])
                new_language = data["programming_language"]
                new_stars = data["rating"]
                new_data = data["description"]
                
                if new_id == None or (Note.query.filter_by(id = new_id).first() != Note.query.filter_by(id = new_id, user_id = user_id).first()):
                    abort(404)    
                elif new_date == None:
                    abort(404)
                elif new_interval == None or  new_interval=="" or int(new_interval) < 1 or int(new_interval) > 1440:
                    abort(404)
                elif new_language == None or new_language.isspace() or len(new_language) < 1 or len(new_language) > 30:
                    abort(404)
                elif new_stars == None or new_stars == "" or int(new_stars) > 5 or int(new_stars) < 0:
                    abort(404)
                elif new_data == None or len(new_data) < 1 or len(new_data) > 300 or new_data.isspace():
                    abort(404)
                else:
                    note.id = new_id
                    note.date = new_date
                    note.interval = new_interval
                    note.language = new_language
                    note.stars = new_stars
                    note.data = new_data
                    db.session.commit()
                    json_soubor = {'id': str(new_id), 'date': str(new_date),'time_spent': str(new_interval), 'programming_language': new_language, 'rating': new_stars, 'description': new_data}
                    return jsonify(json_soubor), 200
        if False:
                abort(404)
        else:
            abort(404)
        
    
    
    if request.method == "DELETE":
        note = Note.query.filter_by(id=record_id, user_id=user_id).first()
        if note:
            db.session.delete(note)
            db.session.commit()
            return "", 200
        else:
            abort(404)
    
    
    if request.method == "GET":
        note = Note.query.filter_by(id=record_id, user_id=user_id).first()
        if note:
            json_soubor = {'id': str(note.id), 'date': note.date.strftime("%Y-%m-%d"),'time_spent': str(note.interval), 'programming_language': note.language, 'rating': note.stars, 'description': note.data}
            return jsonify(json_soubor), 200
        else:
            abort(404)

@api.route("/users/<string:user_id>/records",  methods=['GET', 'POST'])
def records(user_id):
    if request.method == "GET":
        notes = Note.query.filter_by(user_id=user_id).all()
        json_soubor = []
        try:
            if notes:
                for note in notes:
                    json_soubor.append({'id': str(note.id), 'date': note.date.strftime("%Y-%m-%d"),'time_spent': str(note.interval), 'programming_language': note.language, 'rating': note.stars, 'description': note.data})
                return jsonify(json_soubor), 200
            else:
                abort(404)
        except:
            abort(404)
            
    if request.method == "POST":
        note = Note.query.filter_by(user_id=user_id).first()
        if note:
            try:
                data = request.get_json()
                
                new_date = datetime.strptime(data["date"], '%Y-%m-%d').date()
                new_interval = int(data["time_spent"])
                new_language = data["programming_language"]
                new_stars = data["rating"]
                new_data = data["description"]
                  
                if new_date == None:
                    abort(404)
                elif new_interval == None or  new_interval=="" or int(new_interval) < 1 or int(new_interval) > 1440:
                    abort(404)
                elif new_language == None or new_language.isspace() or len(new_language) < 1 or len(new_language) > 30:
                    abort(404)
                elif new_stars == None or new_stars == "" or int(new_stars) > 5 or int(new_stars) < 0:
                    abort(404)
                elif new_data == None or len(new_data) < 1 or len(new_data) > 300 or new_data.isspace():
                    abort(404)
                else:
                    user = Note(id=str(uuid.uuid4()), date=new_date, interval = new_interval, language = new_language, stars = new_stars, data = new_data, user_id = int(user_id))
                    db.session.add(user)
                    db.session.commit()
                    json_soubor = {'id': str(note.id), 'date': note.date.strftime("%Y-%m-%d"),'time_spent': str(note.interval), 'programming_language': note.language, 'rating': note.stars, 'description': note.data}
                    return jsonify(json_soubor), 201
            
            except:
                abort(404)
        else:
            abort(404)