import numpy

from generator.model.model_distribution import ModelDistribution


class NoncentralChisquareDistribution(ModelDistribution):
    def __init__(self, model_description):
        super().__init__(model_description)
        self.df = model_description['df']
        self.nonc = model_description['nonc']

    def generate_values(self):
        value = numpy.random.noncentral_chisquare(self.df, self.nonc, self.count)
        value = list(value)

        if len(value) == 1:
            value = value[0]

        return self.key, value