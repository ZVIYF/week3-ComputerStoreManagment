from .get_string import get_string
from .get_number import get_positive_number, get_integer
from validation_errors.product_validation import valid_product_category
from prints.errors import print_error


def get_product_category():
    valid_category = False
    while not valid_category:          
        category = get_string("Enter product category:")
        try:
            valid_product_category(category)
            valid_category = True
        except ValueError as error:
            print_error(error)
    return category


def gather_product_inputs()-> tuple:
    name = get_string("Enter product name:")
    category = get_product_category()
    price = get_positive_number("Enter product price:")
    quantity = get_integer("Enter quantity in stock:")
    return name, category, price, quantity