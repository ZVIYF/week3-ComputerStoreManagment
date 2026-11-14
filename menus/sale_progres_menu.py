from prints.sales import print_sale_progres_menu
from utils.menu_choice import get_menu_choice
from validation_errors.menu import not_valid_choice
from sales.add_sale import add_sale_item
from sales.update_sale_item_quantity import update_sale_item_quantity
from sales.remove_item_from_sale import remove_item_from_sale
from sales.set_dicount import set_discount


def sale_progres_menu(sale:dict, sales:list, products:list):
    keep_adding = True
    while keep_adding:
        print_sale_progres_menu()
        choice = get_menu_choice()
        match choice:
            case 1:
                add_sale_item(sale, products)
            case 2:
                update_sale_item_quantity(sale, products)
            case 3:
                remove_item_from_sale(sale, products)
            case 4:
                set_discount(sale)
            case 5:
                keep_adding = False
            case _:
                not_valid_choice("1 - 5")

