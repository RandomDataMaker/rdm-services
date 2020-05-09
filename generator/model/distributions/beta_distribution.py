import numpy

from generator.model.model_distribution import ModelDistribution


class BetaDistribution(ModelDistribution):
    def __init__(self, model_description):
        super().__init__(model_description)
        self.a = model_description['a']
        self.b = model_description['b']

    def generate_values(self):
        value = numpy.random.beta(self.a, self.b, self.count)
        value = list(value)

        if len(value) == 1:
            value = value[0]

        return self.key, value
