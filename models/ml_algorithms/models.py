"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 17 January, 2018 @ 3:26 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
import models.ml_algorithms.base as base

import sklearn.svm as svm
import sklearn.tree as tree
import sklearn.ensemble as ensemble
import sklearn.naive_bayes as naive_bayes


class SupportVectorMachine(base.Model):
    def __init__(self, **kwargs):
        super(SupportVectorMachine, self).__init__()

        self.model = svm.SVC(**kwargs)


class DecisionTree(base.Model):
    def __init__(self, **kwargs):
        super(DecisionTree, self).__init__()

        self.model = tree.DecisionTreeClassifier(**kwargs)


class GaussianNB(base.Model):
    def __init__(self, **kwargs):
        super(GaussianNB, self).__init__()

        self.model = naive_bayes.GaussianNB(**kwargs)


class BernoulliNB(base.Model):
    def __init__(self, **kwargs):
        super(BernoulliNB, self).__init__()

        self.model = naive_bayes.BernoulliNB(**kwargs)


class RandomForest(base.Model):
    def __init__(self, **kwargs):
        super(RandomForest, self).__init__()

        self.model = ensemble.RandomForestClassifier(**kwargs)


class AdaBoost(base.Model):
    def __init__(self, **kwargs):
        super(AdaBoost, self).__init__()

        self.model = ensemble.AdaBoostClassifier(**kwargs)


class Bagging(base.Model):
    def __init__(self, **kwargs):
        super(Bagging, self).__init__()

        self.model = ensemble.BaggingClassifier(**kwargs)


class GradientBoosting(base.Model):
    def __init__(self, **kwargs):
        super(GradientBoosting, self).__init__()

        self.model = ensemble.GradientBoostingClassifier(**kwargs)


MODELS = {
    'Decision Tree': DecisionTree,
    'Support Vector Machine': SupportVectorMachine,
    'Gaussian (Naïve Bayes)': GaussianNB,
    'Bernoulli (Naïve Bayes)': BernoulliNB,
    'Bagging (Ensemble)': Bagging,
    'AdaBoost (Ensemble)': AdaBoost,
    'Random Forest (Ensemble)': RandomForest,
    'Gradient Boosting (Ensemble)': GradientBoosting,
}
