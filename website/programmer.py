from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .models import User
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
import json

programmer = Blueprint("programmer", __name__) 

@programmer.route("/pridejprogramatora", methods=["GET","POST"])
@login_required
def add():
    
    if(current_user.role == "Uživatel"):
        return redirect(url_for("import_export.page"))
    
    er_succ_message = "Zpráva"
    trida = "none"
    if request.method == "POST":    
            
        jmeno = request.form.get("AddNewProgrammer1")
        username = request.form.get("AddNewProgrammerUsername1")
        email = request.form.get("AddNewProgrammerEmail1")
        pass1 = request.form.get("AddNewProgrammerPass1")
        pass2 = request.form.get("AddNewProgrammerPass2")
        role = request.form.get("AddNewProgrammerRole1")
    
        if jmeno == None or len(jmeno) < 1 or len(jmeno) > 40 or jmeno.isspace():
            er_succ_message = "Špatně zadané jméno"
            trida = "error"  
        
        elif username == None or len(username) < 1 or len(username) > 40 or username.isspace():
            er_succ_message = "Špatně zadané uživatelské jméno"
            trida = "error"     
        
        elif email == None or len(email) < 2 or len(email) > 100 or email.isspace() or "@" not in email or "i" not in email:
            er_succ_message = "Špatně zadaný email"
            trida = "error"
                               
        elif pass1 == None or len(pass1) < 1 or len(pass1) > 100 or pass1.isspace():
            er_succ_message = "Špatně zadané heslo"
            trida = "error"     
            
        elif pass2 == None or len(pass2) < 1 or len(pass2) > 100 or pass2.isspace():
            er_succ_message = "Špatně zadané heslo"
            trida = "error"        
            
        elif pass1 != pass2:
            er_succ_message = "Hesla se neshodují"
            trida = "error"       
        
        elif role == None or (role != "Uživatel" and role != "Administrátor"):
            er_succ_message = "Špatně zadané heslo"
            trida = "error"      
        
        else:
            er_succ_message = "Programátor byl vytvořen!"
            trida = "success"
            new_programmer = User(jmeno = jmeno, email=email, username=username, role=role,password=generate_password_hash(pass1))
            db.session.add(new_programmer)
            db.session.commit()
                            
    return render_template("add_programmer.html", message = er_succ_message, trida=trida, programmers=User.query.all(), original_programmer = current_user)

@programmer.route("/upravprogramatora/<cislo>", methods=["GET","POST"])
@login_required
def edit(cislo):
    
    if(current_user.role == "Uživatel"):
        return redirect(url_for("import_export.page"))
    
    original_programmer = User.query.filter_by(id=cislo).first_or_404() # Původní programátor
    
    er_succ_message = "Zpráva"
    trida = "none"
    if request.method == "POST":    
        
        jmeno = request.form.get("AddNewProgrammer1")
        username = request.form.get("AddNewProgrammerUsername1")
        email = request.form.get("AddNewProgrammerEmail1")
        pass1 = request.form.get("AddNewProgrammerPass1")
        pass2 = request.form.get("AddNewProgrammerPass2")
        role = request.form.get("AddNewProgrammerRole1")
    
        if jmeno == None or len(jmeno) < 1 or len(jmeno) > 40 or jmeno.isspace():
            er_succ_message = "Špatně zadané jméno"
            trida = "error"  
        
        elif username == None or len(username) < 1 or len(username) > 40 or username.isspace():
            er_succ_message = "Špatně zadané uživatelské jméno"
            trida = "error"     
        
        elif email == None or len(email) < 2 or len(email) > 100 or email.isspace() or "@" not in email or "i" not in email:
            er_succ_message = "Špatně zadaný email"
            trida = "error"
                               
        elif pass1 == None or len(pass1) < 1 or len(pass1) > 100 or pass1.isspace():
            er_succ_message = "Špatně zadané heslo"
            trida = "error"     
            
        elif pass2 == None or len(pass2) < 1 or len(pass2) > 100 or pass2.isspace():
            er_succ_message = "Špatně zadané heslo"
            trida = "error"        
            
        elif pass1 != pass2:
            er_succ_message = "Hesla se neshodují"
            trida = "error"       
        
        elif role == None or (role != "Uživatel" and role != "Administrátor"):
            er_succ_message = "Špatně zadané heslo"
            trida = "error"                       
        
        else:
            er_succ_message = "Programátor byl upraven!"
            trida = "success"
            User.query.filter_by(id=cislo).first_or_404().jmeno = jmeno
            User.query.filter_by(id=cislo).first_or_404().email = email
            User.query.filter_by(id=cislo).first_or_404().username = username
            User.query.filter_by(id=cislo).first_or_404().role = role
            User.query.filter_by(id=cislo).first_or_404().password = generate_password_hash(pass1)
            db.session.commit()
            #return redirect(url_for("views.main_window", user = cislo))

    
    return render_template("edit_programmer.html", user_id = int(cislo), message = er_succ_message, trida=trida, programmers=User.query.all(), original_programmer=original_programmer, current_user = current_user)

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