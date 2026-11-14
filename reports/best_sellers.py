from utils.reports import sales_counter
from prints.reports import print_next_rated, print_header
from validation_errors.reports import valid_sales
from prints.errors import print_error


def best_sellers(sales: list):
    print_header("5 BEST SELLERS")
    try:
        valid_sales(sales)
    except TypeError as error:
        print_error(error)
        return
    products_record = iter(sales_counter(sales, "name"))
    for i in range(1, 6):
        print_next_rated(i, products_record)