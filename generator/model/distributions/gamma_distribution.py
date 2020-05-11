import numpy

from generator.model.model_distribution import ModelDistribution


class GammaDistribution(ModelDistribution):
    def __init__(self, model_description):
        super().__init__(model_description)
        self.shape = model_description['shape']
        self.scale = model_description['scale']

    def generate_values(self):
        value = numpy.random.gamma(self.shape, self.scale, self.count)
        value = list(value)

        if len(value) == 1:
            value = value[0]

        return self.key, value