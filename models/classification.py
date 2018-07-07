"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com

  Created on 17 January, 2018 @ 3:54 PM.

  Copyright © 2018. Victor. All rights reserved.
"""
import os
import pickle

import numpy as np

from helpers.consts import BREAST_CANCER_DATASET, CLASSIFIER_PATH
from helpers.consts import ModeKeys, CLASS_MAPPING
from models.ml_algorithms import models, utils


def process(data: dict=None, **kwargs):
    Models = models.MODELS

    # Machine learning algorithm to use. SVM by default.
    algorithm = kwargs.get('algorithm') or list(Models.keys())[0]

    # Train, test or inference mode?
    mode = kwargs.get('mode') or ModeKeys.INFERENCE
    # `algorithm` must be valid.
    if algorithm not in Models.keys():
        raise KeyError("Got '{}'. Expected one of \"{}\"".format(
            algorithm, '", '.join(Models.keys())))

   # Path to save this classifier
    clf_path = CLASSIFIER_PATH.format(algorithm)
    payload = {}  # return value.

    # For inference:
    if mode.upper() == ModeKeys.INFERENCE.upper():
        if data is None:
            raise ValueError("Supply values to use for inference.")

        # Values used for inference.
        values = np.array(list(map(lambda x: int(x[1][0]), data.items())))

        if not os.path.isfile(clf_path):
            msg = "You haven't trained {}. Go to /settings/ to train it!"
            raise FileNotFoundError(msg.format(algorithm))

        with open(clf_path, 'rb') as f:
            clf = pickle.load(f)

        # Make predictions.
        prediction = int(clf.predict(values)[0])
        payload['prediction'] = CLASS_MAPPING[prediction]
    else:
        # For Training & Testing.

        # Load & pre-process dataset.
        x, y = utils.preprocess(data_dir=BREAST_CANCER_DATASET)

        # Split data into training & testing set.
        X_train, y_train, X_test, y_test = utils.split(x, y, test_size=0.1)
        payload["n_train"], payload["n_test"] = len(y_train), len(y_test)

        if mode.upper() == ModeKeys.TRAIN.upper():
            # Create a new classifier.
            clf = Models[algorithm]()

            # Train classifier on training set.
            clf.train(X_train, y_train)

            # Create save directory if it doesn't exist.
            if not os.path.isdir(os.path.dirname(clf_path)):
                os.makedirs(os.path.dirname(clf_path))

            # Save the trained classifier.
            with open(clf_path, 'wb') as f:
                pickle.dump(clf, f)

        if not os.path.isfile(clf_path):
            msg = "You haven't trained {}. Go to /settings/ to train it!"
            raise FileNotFoundError(msg.format(algorithm))

        # Test model.
        with open(clf_path, 'rb') as f:
            clf = pickle.load(f)

        payload['score'] = '{:.02%}'.format(clf.test(X_test, y_test))

    # Update payload
    payload['error'], payload["algorithm"] = None, algorithm

    return payload
