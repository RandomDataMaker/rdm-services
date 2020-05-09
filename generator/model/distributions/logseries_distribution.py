import numpy

from generator.model.model_distribution import ModelDistribution


class LogseriesDistribution(ModelDistribution):
    def __init__(self, model_description):
        super().__init__(model_description)
        self.p = model_description['p']

    def generate_values(self):
        value = numpy.random.logseries(self.p, self.count)
        value = list(value)

        if len(value) == 1:
            value = value[0]

        return self.key, value