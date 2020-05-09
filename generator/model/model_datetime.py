from generator.model.model_entity import ModelEntity
from datetime import datetime
from random import randrange
from datetime import timedelta


class ModelDateTime(ModelEntity):
    default_date_format = '%m/%d/%Y %I:%M %p'

    def __init__(self, model_description):
        super().__init__(model_description)
        self.min_date = model_description['min_date']
        self.max_date = model_description['max_date']
        self.date_format = self.default_date_format

        if 'date_format' in model_description:
            self.date_format = model_description['date_format']

    def generate_values(self):
        value = []
        for i in range(self.count):
            v = self.__generate_single_value()
            value.append(v.strftime(self.date_format))

        if len(value) == 1:
            value = value[0]

        return self.key, value

    def __generate_single_value(self):
        """
        This function will return a random datetime between two dates
        as strings
        """

        date_start = datetime.strptime(self.min_date, self.date_format)
        date_end = datetime.strptime(self.max_date, self.date_format)
        value = ModelDateTime.__generate_random_datetime(date_start, date_end)

        return value

    @staticmethod
    def __generate_random_datetime(start, end):
        """
        This function will return a random datetime between two datetime
        objects.
        """
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)

        return start + timedelta(seconds=random_second)
