"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 12 January, 2018 @ 4:25 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import render_template, request, escape

from models import classification as clf
from views import app, back


@app.route('/')
@back.anchor
def index():
    return render_template('index.html')


@app.route('/about/')
@back.anchor
def about():
    return render_template('about.html')


@app.route('/contact/', methods=['GET'])
@back.anchor
def contact():
    if request.method == 'POST':
        return render_template('contact.html')
    return render_template('contact.html')


@app.route('/appointment/', methods=['GET'])
@back.anchor
def appointment():
    return render_template('appointment.html')


@app.route('/classification/', methods=['GET'])
@back.anchor
def classification(result=None):
    if result:
        print(result)
    return render_template('classification.html')


@app.route('/typography/')
@back.anchor
def typography():
    return render_template('typography.html')


@app.route('/single/')
def single():
    return render_template('single.html')
