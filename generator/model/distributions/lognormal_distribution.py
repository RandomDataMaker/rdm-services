import numpy

from generator.model.model_distribution import ModelDistribution


class LognormalDistribution(ModelDistribution):
    def __init__(self, model_description):
        super().__init__(model_description)
        self.mean = model_description['mean']
        self.sigma = model_description['sigma']

    def generate_values(self):
        value = numpy.random.lognormal(self.mean, self.sigma, self.count)
        value = list(value)

        if len(value) == 1:
            value = value[0]

        return self.key, value