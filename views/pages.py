"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 12 January, 2018 @ 4:25 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import render_template, redirect, url_for

from views import app, back


@app.route('/')
@back.anchor
def index():
    return render_template('index.html')


@app.route('/about/')
@back.anchor
def about():
    return render_template('about.html')


@app.route('/contact/')
@back.anchor
def contact():
    return render_template('contact.html')


@app.route('/appointment/')
@back.anchor
def appointment():
    return render_template('appointment.html')


@app.route('/icons/')
@back.anchor
def icons():
    return render_template('icons.html')


@app.route('/typography/')
@back.anchor
def typography():
    return render_template('typography.html')


@app.route('/newsletter/', methods=['POST'])
def newsletter():
    return redirect(url_for('index'))
