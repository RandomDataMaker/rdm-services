import numpy

from generator.model.model_distribution import ModelDistribution


class LogisticDistribution(ModelDistribution):
    def __init__(self, model_description):
        super().__init__(model_description)
        self.loc = model_description['loc']
        self.scale = model_description['scale']

    def generate_values(self):
        value = numpy.random.logistic(self.loc, self.scale, self.count)
        value = list(value)

        if len(value) == 1:
            value = value[0]

        return self.key, value