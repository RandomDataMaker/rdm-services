import numpy

from generator.model.model_distribution import ModelDistribution


class HypergeometricDistribution(ModelDistribution):
    def __init__(self, model_description):
        super().__init__(model_description)
        self.ngood = model_description['ngood']
        self.nbad = model_description['nbad']
        self.nsample = model_description['nsample']

    def generate_values(self):
        value = numpy.random.hypergeometric(self.ngood, self.nbad, self.nsample, self.count)
        value = list(value)

        if len(value) == 1:
            value = value[0]

        return self.key, value