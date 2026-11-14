from prints.reports import print_header, report_printer


def total_sales(sales: list):
    print_header("TOTAL SALES")
    total = len(sales)
    report_printer("total", total)
    