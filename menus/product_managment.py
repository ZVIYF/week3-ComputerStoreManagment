from prints.menu_prints import print_product_management_menu
from utils.menu_choice import get_menu_choice
from validation_errors.menu import not_valid_choice
from products.add_product import add_product
from products.show_products import show_products
from products.find_products import find_product
from products.update_product import update_product
from products.delete_product import delete_product



def product_menu(products_list: list[dict]):
    back_to_main = False
    while not back_to_main:
        print_product_management_menu()
        choice = get_menu_choice()
        match choice:
            case 1:
                add_product(products_list)
            case 2:
                show_products(products_list)
            case 3:
                find_product(products_list)
            case 4:
                update_product(products_list)
            case 5:
                delete_product(products_list)
            case 6:
                back_to_main = True
            case _:
                not_valid_choice("1 - 6")