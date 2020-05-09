import random

from generator.model.model_entity import ModelEntity


class ModelRange(ModelEntity):

    def __init__(self, model_description):
        super().__init__(model_description)
        self.minimum = 0
        self.floating_points = 0
        self.maximum = model_description['maximum']

        if 'minimum' in model_description:
            self.minimum = model_description['minimum']
        if 'floating_points' in model_description:
            self.floating_points = model_description['floating_points']

        if self.maximum < self.minimum:
            self.maximum, self.minimum = self.minimum, self.maximum

    def generate_values(self):
        if type(self.maximum) is float or type(self.minimum) is float:
            value = []
            for i in range(self.count):
                v = random.random() * abs(self.maximum - self.minimum) + self.minimum
                value.append(v)
        else:
            value = random.choices(range(self.minimum, self.maximum), k=self.count)

        if self.floating_points is not None:
            for i in range(len(value)):
                value[i] = round(value[i], self.floating_points)

        if len(value) == 1:
            value = value[0]

        return self.key, value
