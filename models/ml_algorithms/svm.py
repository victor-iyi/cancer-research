"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 17 January, 2018 @ 3:26 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from sklearn.svm import SVC


class SVM:
    def __init__(self, **kwargs):

        self.model = SVC(**kwargs)

    def predict(self, X):
        return self.model.predict([X])

    def train(self, X, y):
        self.model.fit(X, y)

    def test(self, X, y):
        return self.model.score(X, y)
