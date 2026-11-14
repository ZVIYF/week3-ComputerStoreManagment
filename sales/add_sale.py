from prints.errors import print_error
from validation_errors.sales import valid_to_add
from inputs.get_sale_item_info import get_valid_id, get_valid_quantity
from products.find_products import search_product_by_id
from utils.sales import update_sale_total, get_product_by_id





def create_sale_item_object(product: dict, quantity: int)-> dict:
    sale_item = {
            "product_id": product["id"],
            "name": product["name"],
            "quantity": quantity,
            "unit_price": product["price"],
            "total": product["price"] * quantity,
            "category": product["category"]
            }
    return sale_item


def add_sale_item(sale: dict, products:list):
    id = get_valid_id(products)
    try:
        valid_to_add(id, sale)
    except ValueError as error:
        print_error(error)
        return    
    product = get_product_by_id(products, id)
    quantity = get_valid_quantity(product)
    sale_item = create_sale_item_object(product, quantity)
    sale["items"].append(sale_item)
    update_sale_total(sale)        
