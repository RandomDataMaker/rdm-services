import numpy

from generator.model.model_distribution import ModelDistribution


class RayleighDistribution(ModelDistribution):
    def __init__(self, model_description):
        super().__init__(model_description)
        self.scale = model_description['scale']

    def generate_values(self):
        value = numpy.random.rayleigh(self.scale, self.count)
        value = list(value)

        if len(value) == 1:
            value = value[0]

        return self.key, value