from prints.products import print_products
from utils.inventory import filter_products_low_stock

def show_out_of_stock(products_list: list):
    out_of_stock = filter_products_low_stock(products_list)
    print_products(out_of_stock)