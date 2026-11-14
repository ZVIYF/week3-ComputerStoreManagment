from prints.sales import print_sale_items
from prints.errors import print_error
from inputs.get_sale_item_info import get_valid_id
from validation_errors.sales import valid_to_change
from utils.sales import get_sale_item_by_id, update_sale_total



def remove_item_from_sale(sale:dict, products: list):
    print_sale_items(sale)
    item_id = get_valid_id(products)
    try:
        valid_to_change(item_id, sale)
    except ValueError as error:
        print_error(error)
        return    
    sale_item = get_sale_item_by_id(sale, item_id)
    sale["items"].remove(sale_item)
    update_sale_total(sale)