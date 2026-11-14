from products.find_products import search_product_by_id
from validation_errors.inventory import valid_amount_to_reduce
from prints.sales import print_quantity_failure


def get_sale_item_by_id(sale:dict, item_id: int)-> dict:
    for item in sale["items"]:
        if item["product_id"] == item_id:
            return item


def update_sale_total(sale):
    sale["subtotal"] = sum(list(map(lambda item: item["total"], sale["items"])))
    sale["total"] = sale["subtotal"] * ((100 - sale["discount"]) / 100)


def check_products_stock(products: list, sale: dict):
    for item in sale["items"]:
        product_id = item["product_id"]
        quantity = item["quantity"]
        product = search_product_by_id(product_id)[0]
        try:
            valid_amount_to_reduce(product["stock"], quantity)
            return True
        except ValueError:
            print_quantity_failure(item, product)
            return False


def update_products_stock(products: list, sale: dict):
    for item in sale["items"]:
        product_id = item["product_id"]
        quantity = item["quantity"]
        product = search_product_by_id(product_id)[0]
        product["stock"] -= quantity


def generate_sale_id(sales: list):
    return len(sales) + 1