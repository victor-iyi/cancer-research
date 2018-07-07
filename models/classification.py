"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 17 January, 2018 @ 3:54 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
import pickle

import numpy as np

from helpers.consts import BREAST_CANCER_DATASET, CLASCLASSIFIER_PATH
from models.ml_algorithms import models
from models.ml_algorithms.utils import preprocess


def process(data, type='svm'):
    values = list(map(lambda x: int(x[1][0]), data.items()))
    values = np.array(values)

    x, y = preprocess(data_dir=BREAST_CANCER_DATASET)

    clf = models.SVM()
    clf.train(x, y)

    prediction = clf.predict(values)
    prediction = int(prediction[0])
    CLASS_NAMES = {2: 'Malignant', 4: 'Benign'}

    return {
        'prediction': CLASS_NAMES[prediction]
    }
