"""
  @author Victor I. Afolabi
  
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 27 January, 2018 @ 1:54 AM.
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import redirect, url_for, request, escape, flash, jsonify
from views import app, back
from models import classification as clf


@app.route('/_newsletter', methods=['POST'])
def newsletter_form():
    email = request.form['email']
    flash(f'Email: {email}')
    return back.redirect()


@app.route('/_contact', methods=['POST'])
def contact_form():
    name = request.form['name']
    email = request.form['email']
    number = request.form['number']
    subject = request.form['subject']
    message = request.form['message']
    flash(f'{name}, {email}, {number}, {subject}, {message}')
    return redirect(url_for('contact'))


@app.route('/_appointment', methods=['POST'])
def appointment_form():
    name = escape(request.form['name'])
    phone = escape(request.form['number'])
    email = escape(request.form['email'])
    date = escape(request.form['date'])
    gender = escape(request.form['gender'])
    time = escape(request.form['time'])
    flash(f'{name}, {phone}, {email}, {date}, {gender}, {time}')
    return redirect(url_for('appointment'))


@app.route('/_classification')
def classification_form():
    # store request form into a Python dictionary.
    data = dict(request.args)
    print(data)
    name = data.pop('name')[0]  # remove 'name' key
    # prediction result
    result = clf.process(data)
    data = {'name': name, 'result': result}
    return jsonify(data=data)
