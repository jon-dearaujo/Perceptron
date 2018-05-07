import random

from point import Point

class Perceptron():
  def __init__(self, weights_size):
    # Initialize ramdomly the weights
    self._weights = [random.random() for i in range(weights_size)]
    self.learning_rate = 1

  def _sign(self, x):
    '''Returms -1 for numbers lest than 0 and 1 for numbers greather than 0. It is the activation function'''
    return 1 if x >= 0 else -1

  def guess(self, inputs):
    '''inputs is an float array'''
    sum = 0
    for index, weight in enumerate(self._weights):
      sum += inputs[index] * weight
    return self._sign(sum)

  def train(self, training_inputs, training_target):
    guess = self.guess(training_inputs)
    error = training_target - guess
    for index, weight in enumerate(self._weights):
      self._weights[index] += error * training_inputs[index] * self.learning_rate

  def __repr__(self):
    return "[weights: {}]".format(str(self._weights))

#end Perceptron

random.seed(1)

training_points = [Point() for i in range(100000)]
perceptron = Perceptron(3)

#start training
for point in training_points:
  perceptron.train([point.x, point.y, point.b], point.label)

#start guessing
test_points = [Point() for i in range(100000)]
success_rate = 0.0
for point in test_points:
  guess = perceptron.guess([point.x, point.y, point.b])
  success_rate = success_rate + 1 if guess == point.label else success_rate

print("success rate: ", (success_rate * 100)/100000)