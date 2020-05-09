from abc import abstractmethod

from generator.model.model_entity import ModelEntity


class ModelDistribution(ModelEntity):
    def __init__(self, model_description):
        super().__init__(model_description)
        self.distribution = model_description['distribution']

    @abstractmethod
    def generate_values(self):
        pass
