from prints.menu_prints import print_update_product_menu
from prints.products import print_products
from utils.menu_choice import get_menu_choice
from validation_errors.menu import not_valid_choice
from inputs.get_product_info import get_string, get_product_category, get_positive_number
from inputs.get_boolean import get_boolean_value


def update_product_menu(product: dict, products_list: list) -> None:
    update_done = False
    while not update_done:
        print_update_product_menu()
        choice = get_menu_choice()
        match choice:
            case 1:
                product["name"] = get_string("Enter product name:")
            case 2:
                product["name"] = get_product_category()
            case 3:
                product["price"] = get_positive_number("Enter product price:")
            case 4:
                product["active"] = get_boolean_value("Is product active?")
            case 5:
                update_done = True
            case _:
                not_valid_choice("1 - 5")
        print_products(list(product))        
