""" Build a perceptron for binary classification """

class Perceptron:
    """ Perceptron  """

    def __init__(self):
        """ Initialize perceptron """
        self._weights = None

    def train(self, inputs, labels):
        """ Train the model with samples of known identity  """
        dummied_inputs = [val + [-1] for val in inputs]
        self._weights = [0.2] * len(dummied_inputs[0])

        for _ in range(5000):
            for value, label in zip(dummied_inputs, labels):
                label_delta = label - self.predict(value)
                for index, val in enumerate(value):
                    self._weights[index] += .1 * val * label_delta

    def predict(self, value):
        """ Classify new samples """
        if len(value) == 0:
            return None
        value = value + [-1]
        assert self._weights is not None, "Run train first"
        return int(0 < sum([row[0]*row[1] for row in zip(self._weights, value)])) #pylint: disable=consider-using-generator
