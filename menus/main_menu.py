from DB.products import PRODUCTS
from DB.sales import SALES

from prints.menu_prints import print_main_menu 
from utils.menu_choice import get_menu_choice
from validation_errors.menu import not_valid_choice
from .product_managment import product_menu
from .inventory_managment import inventory_menu
from .sale_menu import sale_menu
from .reports_menu import reports_menu


def main_menu():
    running = True
    while running:
        print_main_menu()
        choice = get_menu_choice()
        match choice:
            case 1:
                product_menu(PRODUCTS)
            case 2:
                inventory_menu(PRODUCTS)
            case 3:
                sale_menu(SALES, PRODUCTS)
            case 4:
                reports_menu(SALES)
            case 5:
                running = False
            case _:
                not_valid_choice("1 - 5")