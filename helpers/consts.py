"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 06 January, 2018 @ 7:54 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
import os


# Application name.
APP_NAME = 'Cancer-Research'

# Project base directory.
PROJECT_DIR = os.getcwd()

# Path to static directory.
STATIC_DIR = os.path.join(PROJECT_DIR, 'static')

# Path to dataset directory.
DATASET_DIR = os.path.join(STATIC_DIR, 'datasets')

# Path to the breast cancer dataset.
BREAST_CANCER_DATASET = os.path.join(DATASET_DIR, 'breast-cancer-wisconsin')

# Path to trained classifier.
CLASSIFIER_PATH = os.path.join(STATIC_DIR, 'models/{}.pkl')

# Class mapping.
CLASS_MAPPING = {2: 'Malignant', 4: 'Benign'}


class ModeKeys:
    """Predict configurations."""

    TRAIN = 'TRAIN'
    TEST = 'TEST'
    INFERENCE = 'INFERENCE'
    PREDICT = INFERENCE
