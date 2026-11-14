from inputs.get_number import get_positive_number
from validation_errors.sales import valid_discount
from prints.errors import print_error
from prints.sales import print_sale_summary
from utils.sales import update_sale_total


def set_discount(sale: dict):
    valid_discount_percent = False
    while not valid_discount_percent:
        discout = get_positive_number("Enter discount percent: (1-100)")
        try:
            valid_discount(discout)
            valid_discount_percent = True
        except ValueError as error:
            print_error(error)
    sale["discount"] = discout
    update_sale_total(sale)
    print_sale_summary(sale)