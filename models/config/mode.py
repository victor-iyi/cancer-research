"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 06 January, 2018 @ 12:57 AM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from helpers.consts import APP_NAME
from models.config import Config


class Production(Config):
    DATABASE_URI = 'mysql://user@localhost/{}'.format(APP_NAME)


class Development(Config):
    DEBUG = True


class Testing(Config):
    TESTING = True
