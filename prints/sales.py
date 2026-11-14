def print_sale_progres_menu():
    print(
"""

1. Add product to sale
2. Update product quantity
3. Remove product from sale
4. Set discount
5. Back to previous menu

"""
)    



def print_sale_header():
    print("=========== NEW SALE ===========\n\n")


def print_sale_menu():
    print(
"""

1. Continue Shopping
2. Complete Sale
3. Cancel Sale

"""
)


def print_item_add(id: int, quantity: int):
    print(f"Product ID: {id}")
    print(f"Quantity: {quantity}")
    print("Add to cart!")


def print_sale_summary(sale: dict):
    print(
"""

=============== SALE SUMMARY ===============

"""
)
    print(f"Sale ID: {sale["id"]}")
    print()

    for item in sale["items"]:
        print(f"{item["name"].ljust(19)} {str(item["quantity"]).ljust(2)} X {str(item["unit_price"]).ljust(5)} = {item["total"]}")
    
    print("--------------------------------------------")
    print(f"Subtotal:\t\t\t {sale["subtotal"]}")
    print(f"Discount:\t\t\t {sale["discount"]} %")
    print(f"Total:\t\t\t\t {sale["total"]}")

def print_sale_completed():
    print(
"""

============================================
Sale completed successfully!

"""
)


def print_sale_items(sale: dict):
    if not sale["items"]:
        print("No items!")
        return
    print(
"""
===================   SALE ITEMS   ===================
    
"""
    )    

    for item in sale["items"]:
        print(f"Item ID: {str(item["product_id"]).ljust(3)} | Name: {item["name"].ljust(18)} | Quantity: {item["quantity"]}")    


def print_quantity_update(item: dict):
    print(f"Item ID: {str(item["product_id"]).ljust(3)} | Name: {item["name"].ljust(18)} | Quantity: {item["quantity"]}")    
    print("Quantity changed!")


def print_quantity_failure(item: dict, product:dict):
    print(f"Error: Whole proccing checkout, item {item["name"]} had more quantity ({item["quantity"]}) then we have in stock ({product["stock"]}). Cannot complet sale.")
