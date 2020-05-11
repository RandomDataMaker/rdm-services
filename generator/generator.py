from generator.model.distributions.distribution_generator import generate_distribution
from generator.model.model_array import ModelArray
from generator.model.model_datetime import ModelDateTime
from generator.model.model_range import ModelRange


def generate_values_dynamically(model_description):
    if 'array' in model_description:
        model = ModelArray(model_description)

    elif 'maximum' in model_description:
        model = ModelRange(model_description)

    elif 'min_date' and 'max_date' in model_description:
        model = ModelDateTime(model_description)

    elif 'distribution' in model_description:
        model = generate_distribution(model_description)


    else:
        raise Exception("Data model does not match any possible case")

    key, value = model.generate_values()

    return key, value
