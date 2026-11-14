from prints.menu_prints import print_inventory_managment_menu
from utils.menu_choice import get_menu_choice
from validation_errors.menu import not_valid_choice
from inventory.show_full_inventory import show_full_inventory
from inventory.find_in_inventory import find_in_inventory
from inventory.add_to_inventory import add_to_inventory
from inventory.reduce_inventory import reduce_inventory
from inventory.show_out_of_stock import show_out_of_stock
from inventory.show_low_stock import show_low_stock
from utils.inventory import filter_active_products



def inventory_menu(products_list: list):
    back_to_main = False
    active_products = filter_active_products(products_list)
    while not back_to_main:
        print_inventory_managment_menu()
        choice = get_menu_choice()
        match choice:
            case 1:
                show_full_inventory(active_products)
            case 2:
                find_in_inventory(active_products)
            case 3:
                add_to_inventory(active_products)
            case 4:
                reduce_inventory(active_products)
            case 5:
                show_out_of_stock(active_products)
            case 6:
                show_low_stock(active_products)
            case 7:
                back_to_main = True
            case _:
                not_valid_choice("1-7")