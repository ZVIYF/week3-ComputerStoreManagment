from prints.errors import print_error
from prints.products import print_products
from products.find_products import search_product_by_id
from validation_errors.product_validation import valid_ID
from inputs.get_number import get_positive_integer


def add_to_inventory(products_list: list):
    result = search_product_by_id(products_list)
    
    try:    
        valid_ID(result)
    except ValueError as error:
        print_error(error)        
        return

    product = result[0]
    amount_to_add = get_positive_integer("Enter number of new stock to add:")
    product["stock"] += amount_to_add
    
