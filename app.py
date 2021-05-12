#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
PATH = os.path.abspath('.')

UPLOAD_FOLDER = 'partidas/'

app.config['MAX_CONTENT_LENGTH'] = 15024 * 1024

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    for uploaded_file in request.files.getlist('file'):
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
            open('partidas.json','w').close()
            return "Invalid image", 400
    return redirect(url_for('index'))


if __name__ == '__main__':
   app.run(debug = True)
