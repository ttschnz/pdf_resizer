#!/usr/bin/env python3

import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory
import uuid
from werkzeug.utils import secure_filename
from convert import convert_pdf

UPLOAD_FOLDER = './temp'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            id = uuid.uuid4().hex
            new_filename = secure_filename(f"{id}.pdf")
            full_path  =os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
            file.save(full_path)
            if convert_pdf(full_path):
                return redirect(url_for('download_file', name=new_filename, download_name=file.filename))
            else:
                flash('Error converting. Is it a PDF?')
                return redirect(request.url)
    return send_from_directory(".", "upload.html")


@app.route('/uploads/<name>/<download_name>')
def download_file(name, download_name):
    try:
        id = uuid.UUID(name.split(".")[0])
        return send_from_directory(app.config["UPLOAD_FOLDER"], f"{id.hex}.pdf", as_attachment=True, download_name=download_name)
    except:
        flash('Invalid filename')
        return redirect(url_for('upload_file'))


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=3000)