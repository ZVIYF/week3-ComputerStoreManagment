from .find_products import search_product_by_id
from prints.errors import print_error
from prints.products import print_products
from menus.update_product_menu import update_product_menu



def update_product(products_list: list):
    print_products(products_list)
    result = search_product_by_id(products_list)
    try:    
        if not result:
            raise ValueError("Product ID does not exists")
    except ValueError as error:
        print_error(error)        
        return
    update_product_menu(result[0], products_list)
