import numpy

from generator.model.model_distribution import ModelDistribution


class TriangularDistribution(ModelDistribution):
    def __init__(self, model_description):
        super().__init__(model_description)
        self.left = model_description['left']
        self.mode = model_description['mode']
        self.right = model_description['right']

    def generate_values(self):
        value = numpy.random.triangular(self.left, self.mode, self.right, self.count)
        value = list(value)

        if len(value) == 1:
            value = value[0]

        return self.key, value