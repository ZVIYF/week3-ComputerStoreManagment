from utils.sales import generate_sale_id
from utils.sales import check_products_stock, update_products_stock
from prints.sales import print_sale_summary, print_sale_completed
from prints.errors import print_error
from validation_errors.sales import valid_sale


def create_sale_object(sales: list)-> dict:
    sale = {
            "id": generate_sale_id(sales),
            "items": [],
            "subtotal": 0.0,
            "discount": 0.0,
            "total": 0.0
            }
    return sale


def complete_sale(sale: dict, sales: list, products: list):
    try:
        valid_sale(sale)
    except ValueError as error:
        print_error(error)        
        return False
    check_products_stock(products, sale)
    print_sale_summary(sale)
    print_sale_completed()
    update_products_stock(products, sale)
    sales.append(sale)
    return True


