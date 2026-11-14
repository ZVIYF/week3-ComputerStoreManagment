from validation_errors.reports import valid_sales
from prints.errors import print_error
from prints.reports import print_header, report_printer
from utils.reports import calculate_sales_revenue


def sales_average(sales: list):
    print_header("SALES AVERAGE")
    try:
        valid_sales(sales)
    except TypeError as error:
        print_error(error)
        return

    sales_revenue = calculate_sales_revenue(sales)
    total_sales = len(sales)
    report_printer("average", sales_revenue / total_sales)
    