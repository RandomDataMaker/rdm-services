import numpy

from generator.model.model_distribution import ModelDistribution


class NoncentralFDistribution(ModelDistribution):
    def __init__(self, model_description):
        super().__init__(model_description)
        self.dfnum = model_description['dfnum']
        self.dfden = model_description['dfden']
        self.nonc = model_description['nonc']

    def generate_values(self):
        value = numpy.random.noncentral_f(self.dfnum, self.dfden, self.nonc, self.count)
        value = list(value)

        if len(value) == 1:
            value = value[0]

        return self.key, value