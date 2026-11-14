from DB.products import ID_COUNTER
from inputs.get_string import get_string
from validation_errors.search import valid_search_key
from prints.errors import print_error



def genarate_product_id()-> int:
    global ID_COUNTER
    ID_COUNTER += 1
    return ID_COUNTER


def get_search_key():
    valid_key = False
    while not valid_key:
        key = get_string("Enter key for search (ID/Category/Name):").lower()
        try:
            valid_search_key(key)
            valid_key = True
        except ValueError as error:
            print_error(error)
    return key
