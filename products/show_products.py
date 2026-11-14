from prints.products import print_products


def show_products(products_list: list[dict]):
    active_products = filter(lambda p: p["active"] == True, products_list)
    print_products(active_products)