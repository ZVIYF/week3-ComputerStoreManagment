from .find_products import search_product_by_id
from prints.products import print_products, product_deleted
from prints.errors import print_error
from inputs.get_boolean import get_boolean_value
from validation_errors.product_validation import valid_ID


def delete_product(products_list: list):
    
    print_products(products_list)
    result = search_product_by_id(products_list)
    
    try:    
        valid_ID(result)
    except ValueError as error:
        print_error(error)        
        return
    
    product = result[0]
    confirm = get_boolean_value("Are you shure:")
    if confirm:
        products_list.remove(product)
    product_deleted(confirm)
