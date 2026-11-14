from prints.menu_prints import print_reports_menu
from utils.menu_choice import get_menu_choice
from validation_errors.menu import not_valid_choice
from reports.total_sales import total_sales
from reports.sales_revenue import sales_revenue
from reports.best_sellers import best_sellers
from reports.sales_average import sales_average
from reports.sales_history import sales_history
from reports.category_statistics import category_statistics


def reports_menu(sales: list):
    back_to_main = False
    while not back_to_main:
        print_reports_menu()
        choice = get_menu_choice()
        match choice:
            case 1:
                total_sales(sales)
            case 2:
                sales_revenue(sales)
            case 3:
                best_sellers(sales)
            case 4:
                sales_average(sales)
            case 5:
                sales_history(sales)
            case 6:
                category_statistics(sales)
            case 7:
                back_to_main = True
            case _:
                not_valid_choice("1 - 7")