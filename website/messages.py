from flask import Blueprint, render_template, request, redirect, jsonify,url_for
import datetime
from .models import User, Note
from . import db
import json

messages = Blueprint("messages", __name__) 
@messages.route("/pridejzpravu", methods=["GET","POST"])
def original_add():
    return redirect(url_for("messages.add", cislo=1))
    
@messages.route("/pridejzpravu/<cislo>", methods=["GET","POST"])
def add(cislo):
    
    original_programmer = User.query.filter_by(id=cislo).first_or_404() # Původní programátor

    er_succ_message = "Zpráva"
    trida = "none"
    
    if request.method == "POST":
        
        datum = request.form.get("AddDate1")
        jazyk = request.form.get("AddLanguage1")
        cas = request.form.get("AddInterval1")
        hodnoceni = request.form.get("AddStar1")
        programator = request.form.get("AddProgrammer1")
        text = request.form.get("AddText1")
        
        
        # ZAČÁTEK TESTOVÁNÍ VSTUPŮ
        try:
            rok, mesic, den = datum.split("-")
            datetime.datetime(year=int(rok),month=int(mesic),day=int(den))
            neplatneDatum = False
        
        except:
            neplatneDatum = True
        
        if neplatneDatum:
            er_succ_message = "Špatně zadané datum"
            trida = "error"
            
        elif jazyk == None or jazyk.isspace() or len(jazyk) < 1 or len(jazyk) > 20:
             er_succ_message = "Špatně zadaný programovací jazyk!"
             trida = "error"

        elif hodnoceni == None or cas=="" or int(cas) < 1 or int(cas) > 1440:
            er_succ_message = "Špatně zadaný čas!"
            trida = "error"
            
        elif hodnoceni == None or hodnoceni == "" or int(hodnoceni) > 5 or int(hodnoceni) < 1:
            er_succ_message = "Špatně zadané hodnocení!"
            trida = "error"   
            
        elif programator == None or str(programator) == "" or User.query.filter_by(id=int(programator)).count() == 0: # Dodělat!!!
            er_succ_message = "Špatně zvolený programátor!"
            trida = "error"   
        
        elif text == None or len(text) < 1 or len(text) > 300 or text.isspace():
            er_succ_message = "Špatně zadaný text!"
            trida = "error"                           
    
        # KONEC TESTOVÁNÍ VSTUPŮ

        else:
            er_succ_message = "Zpráva byla vytvořena"
            trida = "success"
            datum = datetime.datetime.strptime(datum, '%Y-%m-%d').date()
            new_note = Note(date = datum, language = jazyk, interval = cas, stars = hodnoceni, user_id = programator, data = text)
            db.session.add(new_note)
            db.session.commit()
                    
    return render_template("add_message.html", message = er_succ_message, trida=trida, programmers=User.query.all(), original_programmer = original_programmer)

@messages.route("/upravzpravu/<cislo>", methods=["GET","POST"])
def edit(cislo):
    
    original_message = Note.query.filter_by(id=cislo).first_or_404()
    original_programmer = User.query.filter_by(id=original_message.user_id).first_or_404()
    
    er_succ_message = "Zpráva"
    trida = "none"
    
    if request.method == "POST":
        
        datum = request.form.get("AddDate1")
        jazyk = request.form.get("AddLanguage1")
        cas = request.form.get("AddInterval1")
        hodnoceni = request.form.get("AddStar1")
        programator = request.form.get("AddProgrammer1")
        text = request.form.get("AddText1")
        
        
        # ZAČÁTEK TESTOVÁNÍ VSTUPŮ
        try:
            rok, mesic, den = datum.split("-")
            datetime.datetime(year=int(rok),month=int(mesic),day=int(den))
            neplatneDatum = False
        
        except:
            neplatneDatum = True
        
        if neplatneDatum:
            er_succ_message = "Špatně zadané datum"
            trida = "error"
            
        elif jazyk == None or jazyk.isspace() or len(jazyk) < 1 or len(jazyk) > 20:
             er_succ_message = "Špatně zadaný programovací jazyk!"
             trida = "error"

        elif cas == None or cas=="" or int(cas) < 1 or int(cas) > 1440:
            er_succ_message = "Špatně zadaný čas!"
            trida = "error"
            
        elif hodnoceni == None or hodnoceni == "" or int(hodnoceni) > 5 or int(hodnoceni) < 1:
            er_succ_message = "Špatně zadané hodnocení!"
            trida = "error"   
            
        elif programator == None or str(programator) == "" or User.query.filter_by(id=int(programator)).count() == 0: # Dodělat!!!
            er_succ_message = "Špatně zvolený programátor!"
            trida = "error"   
        
        elif text == None or len(text) < 1 or len(text) > 300 or text.isspace():
            er_succ_message = "Špatně zadaný text!"
            trida = "error"                           
    
        # KONEC TESTOVÁNÍ VSTUPŮ

        else:
            er_succ_message = "Zpráva byla upravena"
            trida = "success"
            datum = datetime.datetime.strptime(datum, '%Y-%m-%d').date()
            Note.query.filter_by(id=cislo).first_or_404().date = datum
            Note.query.filter_by(id=cislo).first_or_404().language = jazyk
            Note.query.filter_by(id=cislo).first_or_404().interval = cas
            Note.query.filter_by(id=cislo).first_or_404().stars = hodnoceni
            Note.query.filter_by(id=cislo).first_or_404().user_id = programator
            Note.query.filter_by(id=cislo).first_or_404().data = text
            db.session.commit()
            
                    
    return render_template("edit_message.html", message = er_succ_message, trida=trida, programmers=User.query.all(), original_message = original_message, original_programmer = original_programmer)

@messages.route("/prectizpravu/<cislo>", methods=["GET","POST"])
def read(cislo):
    
    original_message = Note.query.filter_by(id=cislo).first_or_404()
    original_programmer = User.query.filter_by(id=original_message.user_id).first_or_404()
    
    return render_template("read_message.html", programmers=User.query.all(), original_message = original_message, original_programmer = original_programmer)

@messages.route("/smazzpravu", methods=["POST"])
def delete_note():
    if request.method == 'POST':
        note = json.loads(request.data)
        noteId = note['noteId']
        note = Note.query.get(noteId)
        if note:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})