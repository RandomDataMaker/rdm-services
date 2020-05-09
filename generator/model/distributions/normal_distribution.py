import numpy

from generator.model.model_distribution import ModelDistribution


class NormalDistribution(ModelDistribution):
    def __init__(self, model_description):
        super().__init__(model_description)
        self.mu = model_description['mu']
        self.sigma = model_description['sigma']

    def generate_values(self):
        value = numpy.random.normal(self.mu, self.sigma, self.count)
        value = list(value)

        if len(value) == 1:
            value = value[0]

        return self.key, value
