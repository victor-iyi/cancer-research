"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 17 January, 2018 @ 3:54 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""

import numpy as np

from helpers.consts import BREAST_CANCER_DATASET
from models.ml_algorithms import svm
from models.ml_algorithms.utils import preprocess


def process(data):
    values = list(map(__return_value, data.items()))
    values = np.array(values)

    x, y = preprocess(data_dir=BREAST_CANCER_DATASET)

    clf = svm.SVM()
    clf.train(x, y)
    prediction = clf.predict(values)
    prediction = int(prediction[0])
    CLASS_NAMES = {2: 'malignant', 4: 'benign'}

    return {
        'prediction': CLASS_NAMES[prediction]
    }


def __return_value(data):
    # (name, value)
    value = data[1]
    return int(value[0])
