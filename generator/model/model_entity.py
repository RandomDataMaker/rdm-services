import io
import json
from abc import abstractmethod


class ModelEntity:
    def __init__(self, model_description):
        self.key = model_description['key']
        self.count = 1

        if 'count' in model_description:
            self.count = model_description['count']

    @staticmethod
    def parse_model(filepath):
        with io.open(filepath, encoding='utf-8-sig') as json_data:
            data = json.loads(json_data.read())
            entities = data['model']

            return entities

    @abstractmethod
    def generate_values(self):
        pass
