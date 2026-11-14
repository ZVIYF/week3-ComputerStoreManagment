def valid_string(user_input):
    if not user_input:
        raise ValueError("Please type anything:")


def valid_integer(user_input: str):
    if not user_input.isdigit():
        raise ValueError("Input must be a whole number")


def valid_positive_number(user_input: int|float):
    if not (user_input > 0):
        raise ValueError("Input must be a positive number")


def valid_number(user_input: str):
    for char in user_input:
        if not ((char.isdigit()) or (char == ".")):
            raise ValueError("Input must be a number")

    