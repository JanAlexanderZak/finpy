def expected_loss(probabitlity_default: float, exposure_default: float, loss_default: float):
    """
    :param probabitlity_default: Probability of default for one year ( eg. 4% means every 25 years)
    :param exposure_default: Value of credit in given year
    :param loss_default: how much is lost if credit defaults ( eg. loss_default = 25% means 75% is lost
    :return: expected loss for given year
    """
    return probabitlity_default * exposure_default * (1 - loss_default)
