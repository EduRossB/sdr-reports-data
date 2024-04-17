# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, request, redirect, url_for
import pandas as pd
from flask_login import login_required

blueprint = Blueprint("user", __name__, url_prefix="/users", static_folder="../static")

@blueprint.route("/")
@login_required
def members():
    """List members."""
    return render_template("users/members.html")

# Añadimos una nueva ruta para la carga y visualización de archivos Excel
@blueprint.route("/upload", methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            df = pd.read_excel(file, engine='openpyxl')
            # Suponiendo que tienes un template llamado display.html para mostrar los datos
            return render_template("users/display.html", data=df.to_html(classes='table table-striped'))
    return render_template("users/upload.html")
