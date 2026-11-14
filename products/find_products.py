from inputs.get_string import get_string
from inputs.get_product_info import get_product_category
from inputs.get_number import get_positive_integer
from utils.products import get_search_key
from prints.products import print_products



def find_product(products_list: list[dict])-> None:
    results = search_product(products_list)
    print_products(results)
    

def search_product(products_list: list[dict])-> list:
    search_key = get_search_key()
    match search_key:
        case "id":
            return search_product_by_id(products_list)
        case "category":
            return search_by_category(products_list)
        case "name":
            return search_product_by_name(products_list)
    

def search_product_by_name(products_list: list)-> list:
    search_name = get_string("Enter products name")
    return list(filter(lambda p: search_name.lower() in p["name"].lower(), products_list))


def search_product_by_id(products_list: list)-> list:
    searched_id = get_positive_integer("Enter product ID:")
    return list(filter(lambda p: p["id"] == searched_id, products_list))


def search_by_category(products_list: list)-> list:
    searched_category = get_product_category()
    return list(filter(lambda p: p["category"] == searched_category, products_list))


def search_product_by_full_name(products_list: list)-> list:
    search_name = get_string("Enter products name")
    return list(filter(lambda p: p["name"].lower() == search_name.lower(), products_list))
