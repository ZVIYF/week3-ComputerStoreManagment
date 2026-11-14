from .get_string import get_string
from validation_errors.inputs import valid_number, valid_integer, valid_positive_number
from prints.errors import print_error


def get_number(messege: str)-> float:
    is_number = False
    while not is_number:
        user_input = get_string(messege)
        try:
            valid_number(user_input)
            is_number = True
        except ValueError as error:
            print_error(error)
    return float(user_input)


def get_integer(messege: str)-> int:
    is_integer = False
    while not is_integer:
        user_input = get_string(messege)
        try:
            valid_integer(user_input)
            is_integer = True
        except ValueError as error:
            print_error(error)
    return int(user_input)


def get_positive_number(messege: str)-> float:
    is_positive = False
    while not is_positive:
        number = get_number(messege)
        try:
            valid_positive_number(number)
            is_positive = True
        except ValueError as error:
            print_error(error)
    return number


def get_positive_integer(messege: str):
    is_positive = False
    while not is_positive:
        integer = get_integer(messege)
        try:
            valid_positive_number(integer)
            is_positive = True
        except ValueError as error:
            print_error(error)
    return integer


