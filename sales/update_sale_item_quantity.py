from products.find_products import search_product_by_id
from inputs.get_sale_item_info import get_valid_quantity
from prints.sales import print_sale_items, print_quantity_update
from prints.errors import print_error
from validation_errors.sales import valid_to_change
from inputs.get_sale_item_info import get_valid_id
from utils.sales import get_sale_item_by_id, update_sale_total, get_product_by_id



def update_sale_item_quantity(sale: dict, products: list):
    print_sale_items(sale)
    item_id = get_valid_id(products)
    try:
        valid_to_change(item_id, sale)
    except ValueError as error:
        print_error(error)
        return    
    product = get_product_by_id(products, item_id)
    sale_item = get_sale_item_by_id(sale, item_id)
    quantity = get_valid_quantity(product)
    sale_item["quantity"], sale_item["total"] = quantity, quantity * sale_item["unit_price"]    
    print_quantity_update(sale_item)
    update_sale_total(sale)