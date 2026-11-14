from prints.errors import print_error


def not_valid_choice(range:str):
    try:
        raise ValueError(f"Choice must be between {range}")
    except ValueError as error:
        print_error(error)