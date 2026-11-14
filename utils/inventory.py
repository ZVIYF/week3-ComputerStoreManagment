def filter_active_products(products_list: list)-> list:
    return list(filter(lambda p: p["active"]))


def filter_products_in_stock(products_list: list)-> list:
    return list(filter(lambda p: p["stock"] > 0, products_list))


def filter_products_low_stock(products_list: list, low_range = 0)-> list:
    return list(filter(lambda p: p["stock"] <= low_range, products_list))


