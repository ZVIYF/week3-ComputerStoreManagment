from inputs.get_number import get_positive_integer
from utils.inventory import filter_products_low_stock
from prints.products import print_products


def show_low_stock(products_list: list):
    threshold = get_positive_integer("Set low stock threshold:")
    low_stock = filter_products_low_stock(products_list, low_range=threshold)
    print_products(low_stock)