"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 06 January, 2018 @ 7:54 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
import os

APP_NAME = 'breast_cancer'

PROJECT_DIR = os.getcwd()

STATIC_DIR = os.path.join(PROJECT_DIR, 'static')
DATASET_DIR = os.path.join(STATIC_DIR, 'datasets')

BREAST_CANCER_DATASET = os.path.join(DATASET_DIR, 'breast-cancer-wisconsin')
