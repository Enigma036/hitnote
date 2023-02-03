from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .models import User
from . import db
import json

programmer = Blueprint("programmer", __name__) 

@programmer.route("/pridejprogramatora", methods=["GET","POST"])
def add():
    er_succ_message = "Zpráva"
    trida = "none"
    if request.method == "POST":    
            
        jmeno = request.form.get("AddNewProgrammer1")
    
        if jmeno == None or len(jmeno) < 1 or len(jmeno) > 30 or jmeno.isspace():
            er_succ_message = "Špatně zadané jméno"
            trida = "error"                           
        
        elif User.query.filter_by(jmeno=jmeno).count() > 0:
            er_succ_message = "Uživatel se stejným jménem byl již zadán!"
            trida = "error"            
        
        else:
            er_succ_message = "Programátor byl vytvořen!"
            trida = "success"
            new_programmer = User(jmeno = jmeno)
            db.session.add(new_programmer)
            db.session.commit()
                            
    return render_template("add_programmer.html", message = er_succ_message, trida=trida, programmers=User.query.all())

@programmer.route("/upravprogramatora/<cislo>", methods=["GET","POST"])
def edit(cislo):
    
    original_programmer = User.query.filter_by(id=cislo).first_or_404() # Původní programátor
    
    er_succ_message = "Zpráva"
    trida = "none"
    if request.method == "POST":    
            
        jmeno = request.form.get("AddNewProgrammer1")
    
        if jmeno == None or len(jmeno) < 1 or len(jmeno) > 30 or jmeno.isspace():
            er_succ_message = "Špatně zadané jméno"
            trida = "error"                           
        
        elif User.query.filter_by(jmeno=jmeno).count() > 0:
            er_succ_message = "Uživatel se stejným jménem byl již zadán!"
            trida = "error"            
        
        else:
            er_succ_message = "Programátor byl upraven!"
            trida = "success"
            User.query.filter_by(id=cislo).first_or_404().jmeno = jmeno
            db.session.commit()
            return redirect(url_for("views.main_window", user = cislo))

    
    return render_template("edit_programmer.html", message = er_succ_message, trida=trida, programmers=User.query.all(), original_programmer=original_programmer)

@programmer.route("/smazprogramatora", methods=["POST"])
def delete_programmer():
    if request.method == 'POST':
        user = json.loads(request.data)
        UserId = user['userId']
        if UserId != 1:
            user = User.query.get(UserId)
            notes = User.query.filter_by(id=UserId).first_or_404().notes
            
            if notes:
                for note in notes:
                    db.session.delete(note)
                db.session.commit()    
            
            if user:
                db.session.delete(user)
                db.session.commit()
    return jsonify({})