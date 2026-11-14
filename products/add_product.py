from inputs.get_product_info import gather_product_inputs
from prints.products import print_single_product
from utils.products import genarate_product_id

def add_product(products_list: list)-> None:
    product = create_product_object(products_list)
    print_single_product(product)
    products_list.append(product)


def create_product_object(products_list: list) -> dict:
    name, category, price, stock = gather_product_inputs()    
    product = {
    "id": genarate_product_id(),
    "name": name,
    "category": category,
    "price": price,
    "stock": stock,
    "active": True
    }
    return product


