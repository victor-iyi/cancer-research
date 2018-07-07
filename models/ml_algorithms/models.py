"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 17 January, 2018 @ 3:26 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
import models.ml_algorithms.base as base

from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB


class SVM(base.Model):
    def __init__(self, **kwargs):
        super(SVM, self).__init__()

        self.model = SVC(**kwargs)


class NaiveBayes(base.Model):
    def __init__(self, **kwargs):
        super(NaiveBayes, self).__init__()

        self.model = GaussianNB(**kwargs)


class DecisionTree(base.Model):
    def __init__(self, **kwargs):
        super(DecisionTree, self).__init__()

        self.model = DecisionTreeClassifier(**kwargs)


class RandomForest(base.Model):
    def __init__(self, **kwargs):
        super(RandomForest, self).__init__()

        self.model = RandomForestClassifier(**kwargs)


MODELS = {
    'Support Vector Machine': SVM,
    'Naïve Bayes': NaiveBayes,
    'Random Forest': RandomForest,
    'Decision Tree': DecisionTree,
    'Random Foreset': RandomForest,
}
