from utils.reports import calculate_sales_revenue
from prints.reports import print_header, report_printer
from validation_errors.reports import valid_sales
from prints.errors import print_error


def sales_revenue(sales: list):
    print_header("5 BEST SELLERS")
    try:
        valid_sales(sales)
    except TypeError as error:
        print_error(error)
        return
    sales_revenue = calculate_sales_revenue(sales)
    report_printer("revenue", sales_revenue)
    
    
