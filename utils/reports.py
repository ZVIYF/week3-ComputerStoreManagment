def sales_counter(sales: list, key:str)-> list:
    products_counter = {}
    for sale in sales:
        for item in sale["items"]:
            if not item[key] in products_counter:
                products_counter[item[key]] = 0
            products_counter[item[key]] += item["quantity"]
    products_record = [(name, units) for name, units in products_counter.items()]
    return sorted(products_record, key=lambda p: p[1], reverse=True)


def calculate_sales_revenue(sales: list):
    return sum(list(map(lambda sale: sale["total"], sales)))