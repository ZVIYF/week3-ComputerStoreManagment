from prints.reports import print_header
from validation_errors.reports import valid_sales
from prints.errors import print_error
from prints.sales import print_sale_summary


def sales_history(sales):
    print_header("SALES HISTORY")
    try:
        valid_sales(sales)
    except TypeError as error:
        print_error(error)
        return
    for sale in sales:
        print_sale_summary(sale)
        print()
    