"""
  @author Victor I. Afolabi
  
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 27 January, 2018 @ 1:54 AM.
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import redirect, url_for, request, flash, jsonify
from views import app, back
from models import classification as clf


@app.route('/_newsletter', methods=['POST'])
def newsletter_form():
    email = request.form['email']
    flash('Email: {}'.format(email))
    return back.redirect()


@app.route('/_contact', methods=['POST'])
def contact_form():
    name = request.form['name']
    email = request.form['email']
    number = request.form['number']
    subject = request.form['subject']
    message = request.form['message']
    # flash(f'{name}, {email}, {number}, {subject}, {message}')
    return redirect(url_for('contact'))


@app.route('/_classification')
def classification_form():
    # store request form into a Python dictionary.
    data = dict(request.args)
    algorithm = data.pop('algorithm')[0]  # remove 'name' key

    try:
        # prediction result
        payload = clf.process(data=data, algorithm=algorithm)
    except Exception as e:
        payload = {"error": str(e)}

    return jsonify(payload=payload)


@app.route('/_settings')
def settings_form():
    # store request form into a Python dictionary.
    data = dict(request.args)

    # Retrieve data.
    algorithm = data.pop("algorithm")[0]
    mode = data.pop("mode")[0]

    try:
        # Process train/test.
        payload = clf.process(algorithm=algorithm,
                              mode=mode)
    except Exception as e:
        payload = {"error": str(e)}

    return jsonify(payload=payload)
