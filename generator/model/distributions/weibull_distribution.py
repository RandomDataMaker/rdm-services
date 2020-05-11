import numpy

from generator.model.model_distribution import ModelDistribution


class WeibullDistribution(ModelDistribution):
    def __init__(self, model_description):
        super().__init__(model_description)
        self.a = model_description['a']

    def generate_values(self):
        value = numpy.random.weibull(self.a, self.count)
        value = list(value)

        if len(value) == 1:
            value = value[0]

        return self.key, value