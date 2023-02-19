from flask import Blueprint, render_template, redirect, url_for, jsonify, request
from flask_login import login_required, current_user
from datetime import datetime
from .models import Note, User
from website import create_first_user
from .sort_and_filtration import filtrateNotes, getFormData, getSortData, sort_items
from . import db
from sqlalchemy import desc



import_export = Blueprint("import_export", __name__) 

@import_export.route("/importexport")
@login_required
def page():
    
    return render_template("import_export.html", programmer = current_user)
    
