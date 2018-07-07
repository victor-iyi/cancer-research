"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 17 January, 2018 @ 3:31 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""

import os

import numpy as np
import pandas as pd


from sklearn.model_selection import train_test_split


def preprocess(data_dir):
    """
    Processes dataset to return features and labels

    :param data_dir:
        Directory containing datafiles and names
    :return: features, labels
    """

    # noinspection PyBroadException
    try:
        data_files = __list_files(data_dir)
        data_file = __extract_data_file(data_files)

        df = pd.read_csv(data_file)
        df.replace('?', 0, inplace=True)
        df.drop(['id'], axis=1, inplace=True)

        # Split into features and labels
        features = np.array(df.drop(['class'], axis=1), dtype=np.float32)
        labels = np.array(df['class'], dtype=np.float32)

        return features, labels

    except Exception as e:
        print('ERROR: {}'.format(e))
        return False


def split(X, y, test_size=0.1, **kwargs):
    train, test = train_test_split(X, y, test_size=test_size, **kwargs)
    return train, test


def __list_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory)]


def __extract_data_file(data_files):
    for df in data_files:
        if df.endswith('.data.txt'):
            return df
    raise Exception('No data files in this directory')
