from validation_errors.inputs import valid_string
from prints.errors import print_error


def get_string(messege):
    is_string = False
    while not is_string:
        user_input = input(messege).strip()
        try:
            valid_string(user_input)
            is_string = True
        except ValueError as error:
            print_error(error)
    return user_input