from .get_string import get_string
from validation_errors.menu import not_valid_choice


def get_boolean_value(messege: str)-> bool:
    valid_choice = False
    while not valid_choice:
        choice = get_string(f"{messege} (Y/N)").lower().strip()
        match choice:
            case "y":
                return True
            case "n":
                return False
            case _:
                not_valid_choice("Y/N")
