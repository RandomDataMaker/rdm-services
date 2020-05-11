import numpy

from generator.model.model_distribution import ModelDistribution


class PoissonDistribution(ModelDistribution):
    def __init__(self, model_description):
        super().__init__(model_description)
        self.lam = model_description['lam']

    def generate_values(self):
        value = numpy.random.poisson(self.lam, self.count)
        value = list(value)

        if len(value) == 1:
            value = value[0]

        return self.key, value