from products.find_products import search_product_by_id
from validation_errors.product_validation import valid_ID
from prints.errors import print_error
from inputs.get_number import get_positive_integer
from validation_errors.inventory import valid_amount_to_reduce


def reduce_inventory(products_list: list):
    result = search_product_by_id(products_list)
    
    try:    
        valid_ID(result)
    except ValueError as error:
        print_error(error)        
        return

    product = result[0]
    amount_to_reduce = get_positive_integer("Enter quantity to reduce from stock:")

    try:
        valid_amount_to_reduce(product["stock"], amount_to_reduce)
    except ValueError as error:
        print_error(error)
        return
    product["stock"] -= amount_to_reduce