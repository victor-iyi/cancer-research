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
        raise KeyError("Got '{}'. Expected one of '{}'".format(
            algorithm, '", '.join(Models.keys())))

   # Path to save this classifier
    clf_path = CLASSIFIER_PATH.format(algorithm)
    result = {}  # return value.

    # For inference:
    if mode == ModeKeys.INFERENCE:
        if data is None:
            raise ValueError("Supply values to use for inference.")

        # Values used for inference.
        values = np.array(list(map(lambda x: int(x[1][0]), data.items())))

        if not os.path.isfile(clf_path):
            raise FileNotFoundError("You haven't trained this classifier")

        with open(clf_path, 'rb') as f:
            clf = pickle.load(f)

        # Make predictions.
        prediction = int(clf.predict(values)[0])
        result['prediction'] = CLASS_MAPPING[prediction]
    else:
        # For Training & Testing.

        # Load & pre-process dataset.
        x, y = utils.preprocess(data_dir=BREAST_CANCER_DATASET)

        # Split data into training & testing set.
        train, test = utils.split(x, y, test_size=0.1)

        if mode == ModeKeys.TRAIN:
            # Create a new classifier.
            clf = Models[algorithm]()

            # Train classifier on training set.
            clf.train(*train)

            # Create save directory if it doesn't exist.
            if not os.path.isdir(os.path.dirname(clf_path)):
                os.makedirs(clf_path)

            # Save the trained classifier.
            with open(clf_path, 'wb') as f:
                pickle.dump(clf, f)

        if not os.path.isfile(clf_path):
            raise FileNotFoundError("{} hasn't been trained.".format(clf_path))

        # Test model.
        with open(clf_path) as f:
            clf = pickel.load(f)

        result['score'] = clf.test(*test)

    return result
