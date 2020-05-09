from generator.model.distributions.normal_distribution import NormalDistribution


def generate_distribution(distribution_description):
    if distribution_description['distribution'] == 'normal':
        distribution = NormalDistribution(distribution_description)
    else:
        distribution = None

    return distribution
