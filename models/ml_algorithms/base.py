"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 17 January, 2018 @ 3:26 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""


from sklearn.metrics import confusion_matrix


class Model:
    def __init__(self):
        self.model = None

    def __repr__(self):
        return repr(self.model)

    def __str__(self):
        return str(self.model)

    def __call__(self, X):
        return self.predict(X)

    def predict(self, X):
        assert self.model is not None, '`self.model` can\'t be `None`.'

        return self.model.predict([X])

    def train(self, X, y):
        assert self.model is not None, '`self.model` can\'t be `None`.'

        self.model.fit(X, y)

    def test(self, X, y):
        assert self.model is not None, '`self.model` can\'t be `None`.'

        return self.model.score(X, y)

    def metrics(y_true, y_pred, **kwargs):
        return confusion_matrix(y_true=y_true, y_pred=y_pred, **kwargs)
