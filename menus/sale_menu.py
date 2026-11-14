from utils.inventory import filter_active_products
from sales.sales_managment import create_sale_object, complete_sale
from prints.sales import print_sale_header, print_sale_menu
from utils.menu_choice import get_menu_choice
from validation_errors.menu import not_valid_choice
from .sale_progres_menu import sale_progres_menu



def sale_menu(sales: list, products: list):
    sale = create_sale_object(sales)
    active_products = filter_active_products(products)
    print_sale_header()
    sale_complete = False
    while not sale_complete:
        print_sale_menu()
        choice = get_menu_choice()
        match choice:
            case 1:
                sale_progres_menu(sale, sales, active_products)
            case 2:
                sale_complete = complete_sale(sale, sales, active_products)
            case 3:
                sale_complete = True
            case _:
                not_valid_choice("1 - 3")