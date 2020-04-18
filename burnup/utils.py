import statistics
from enum import IntEnum
from typing import Union, List

############################################################
# used to parse feature files, also used to parse GET parameters
# see https://behave.readthedocs.io/en/latest/parse_builtin_types.html
def parse_list_of_number(text):
    """
    Convert parsed text into a list of number.
    :param text: Parsed text, called by :py:meth:`parse.Parser.parse()`.
    :return: Number instance (integer), created from parsed text.
    """
    if ',' in text:
        separator = ','
    elif ';' in text:
        separator = ';'
    else:
        separator = ' '
    result = [int(i) for i in list(text.split(separator))]
    return result


############################################################

class CalculusType(IntEnum):
    XBESTWORST = 1
    STANDARDDEV = 2


def lowest_average_over_last_six_values(numbers) -> float:
    list_length: int = len(numbers)

    result = None
    if list_length < 3:
        result = round(statistics.mean(numbers), 2)
    elif list_length > 6:
        numbers = numbers[list_length - 6:list_length]
        numbers.sort()
        result = round(statistics.mean([numbers[0], numbers[1], numbers[2]]), 2)
    else:
        numbers.sort()
        result = round(statistics.mean([numbers[0], numbers[1], numbers[2]]), 2)

    return result


def highest_average_over_last_six_values(numbers) -> float:
    list_length: int = len(numbers)

    result = None
    if list_length < 3:
        result = round(statistics.mean(numbers), 2)
    elif list_length > 6:
        numbers = numbers[list_length - 6:list_length]
        numbers.sort(reverse=True)
        result = round(statistics.mean([numbers[0], numbers[1], numbers[2]]), 2)
    else:
        numbers.sort(reverse=True)
        result = round(statistics.mean([numbers[0], numbers[1], numbers[2]]), 2)

    return result


def average_over_last_six_values(numbers) -> float:
    list_length: int = len(numbers)

    result = None
    if list_length < 3:
        result = round(statistics.mean(numbers), 2)
    elif list_length > 6:
        numbers = numbers[list_length - 6:list_length]
        numbers.sort(reverse=True)
        result = round(statistics.mean(numbers), 2)
    else:
        numbers.sort(reverse=True)
        result = round(statistics.mean(numbers), 2)

    return result


def get_best_forecast(list, calculus=CalculusType.XBESTWORST) -> List:
    high_average = []
    if calculus == calculus.STANDARDDEV:
        high_average = average_standarddev(list)
    else:
        high_average = highest_average_over_last_six_values(list)

    forecast = []
    for i in range(6):
        if i == 0:
            forecast.append(round(sum(list) + high_average, 2))
        else:
            forecast.append(round(forecast[i - 1] + high_average, 2))
    return forecast


def get_worst_forecast(list, calculus=CalculusType.XBESTWORST) -> List:
    worst_average = []
    if calculus == calculus.STANDARDDEV:
        worst_average = average_standarddev(list)
    else:
        worst_average = lowest_average_over_last_six_values(list)

    forecast = []
    for i in range(6):
        if i == 0:
            forecast.append(round(sum(list) + worst_average, 2))
        else:
            forecast.append(round(forecast[i - 1] + worst_average, 2))
    return forecast


def average_standarddev(numbers) -> float:
    list_length: int = len(numbers)

    if list_length > 6:
        numbers = numbers[list_length - 6:list_length]
        numbers.sort(reverse=True)
        result = round(statistics.stdev(numbers), 2)
    else:
        numbers.sort(reverse=True)
        result = round(statistics.stdev(numbers), 2)

    return result


def get_average_forecast(list, calculus=CalculusType.XBESTWORST):
    average = 0
    if calculus == calculus.STANDARDDEV:
        average = average_standarddev(list)
    else:
        average = average_over_last_six_values(list)

    forecast = []
    for i in range(6):
        if i == 0:
            forecast.append(round(sum(list) + average, 2))
        else:
            forecast.append(round(forecast[i - 1] + average, 2))
    return forecast


def get_real_progress(list):
    real = []
    for idx, val in enumerate(list):
        if idx == 0:
            real.append(val)
        else:
            real.append(real[idx - 1] + val)
    return real
