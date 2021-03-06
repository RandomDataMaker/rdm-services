import numpy

from generator.model.model_distribution import ModelDistribution


class FDistribution(ModelDistribution):
    def __init__(self, model_description):
        super().__init__(model_description)
        self.dfnum = model_description['dfnum']
        self.dfden = model_description['dfden']

    def generate_values(self):
        value = numpy.random.f(self.dfnum, self.dfden, self.count)
        value = list(value)

        if len(value) == 1:
            value = value[0]

        return self.key, value
