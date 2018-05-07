import random

def _f(x):
  '''
  Expected function used to initialize the training/testing data
  The model must be able to find this function.

  This is the function used to determine the class of the training data points,
  so that the model must be able to generate an aproximation of this to predict new values
  '''

  # y = mx + b
  return 1 * x - 0.5

class Point():
  def __init__(self):
    self.x = random.uniform(-1, 1)
    self.y = random.uniform(-1, 1)
    self.b = 1.0

    line = _f(self.x)

    self.label = 1 if self.y > line else -1

  def __repr__(self):
    return '[x: {0}, y: {1}, label: {2}]\n'.format(self.x, self.y, self.label)
