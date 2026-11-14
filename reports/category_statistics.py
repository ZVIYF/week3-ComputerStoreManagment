from utils.reports import sales_counter
from prints.reports import print_next_rated, print_header
from validation_errors.reports import valid_sales
from prints.errors import print_error


def category_statistics(sales:list):

    print_header("CATEGORY STATISTICS")
    try:
        valid_sales(sales)
    except TypeError as error:
        print_error(error)
        return
    category_record = sales_counter(sales, "category")
    category_iter = iter(category_record)
    for i in range(len(category_record)):
        print_next_rated(i + 1, category_iter)