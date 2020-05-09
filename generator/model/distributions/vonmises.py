import numpy

from generator.model.model_distribution import ModelDistribution


class VonmisesDistribution(ModelDistribution):
    def __init__(self, model_description):
        super().__init__(model_description)
        self.mu = model_description['mu']
        self.kappa = model_description['kappa']

    def generate_values(self):
        value = numpy.random.vonmises(self.mu, self.kappa, self.count)
        value = list(value)

        if len(value) == 1:
            value = value[0]

        return self.key, value