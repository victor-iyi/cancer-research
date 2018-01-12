"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 12 January, 2018 @ 3:41 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import Flask

app = Flask('__main__')
app.config.from_object('models.config.Development')

# noinspection PyUnresolvedReferences
from helpers import back

# External routes/views
from views.pages import *
from views.error import *
