from validation_errors.product_validation import valid_ID
from validation_errors.inventory import valid_amount_to_reduce
from inputs.get_number import get_positive_integer
from prints.errors import print_error
from products.find_products import search_product_by_id


def get_valid_quantity(product):
    Valid_quantity = False
    while not Valid_quantity:
        quantity = get_positive_integer("Enter quantity you want to buy:")

        try:
            valid_amount_to_reduce(product["stock"], quantity)
            Valid_quantity = True
        except ValueError as error:
            print_error(error)
    return quantity


def get_valid_id(products: list):
        valid_product = False
        while not valid_product:
                result = search_product_by_id(products)

                try:    
                        valid_ID(result)
                        valid_product = True
                except ValueError as error:
                        print_error(error)
        return result[0]["id"]
