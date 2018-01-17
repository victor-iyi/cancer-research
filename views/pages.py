"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 12 January, 2018 @ 4:25 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import render_template, request, escape

from views import app, back


@app.route('/')
@back.anchor
def index():
    return render_template('index.html')


@app.route('/about/')
@back.anchor
def about():
    return render_template('about.html')


@app.route('/contact/', methods=['GET', 'POST'])
@back.anchor
def contact():
    if request.method == 'POST':
        return render_template('contact.html')
    return render_template('contact.html')


@app.route('/appointment/', methods=['GET', 'POST'])
@back.anchor
def appointment():
    if request.method == 'POST':
        name = escape(request.form['name'])
        phone = escape(request.form['number'])
        email = escape(request.form['email'])
        date = escape(request.form['date'])
        gender = escape(request.form['gender'])
        time = escape(request.form['time'])
        print(name, phone, email, date, gender, time)
        return render_template('appointment.html')
    return render_template('appointment.html')


@app.route('/icons/')
@back.anchor
def icons():
    return render_template('icons.html')


@app.route('/typography/')
@back.anchor
def typography():
    return render_template('typography.html')


@app.route('/single/')
def single():
    return render_template('single.html')


################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Post request methods
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
@app.route('/newsletter/', methods=['POST'])
def newsletter():
    return back.redirect()
