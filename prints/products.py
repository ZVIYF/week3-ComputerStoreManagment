test = [
    {"id": 1, "name": "Gaming Mouse", "category": "Gaming", "price": 150.0, "stock": 20, "active": True},
    {"id": 2, "name": "Mechanical Keyboard", "category": "Accessories", "price": 350.0, "stock": 10, "active": True}
    ]

def print_product(product: dict)-> None:    
    print(f"| \t{product["id"]}\t|  {product["name"].ljust(25)} |  {product["price"]}\t |  {product["stock"]}\t\t |  {product["active"]}\t|")


def print_single_product(product):
    print_products_header()
    print_product(product)


def print_products_header():
    print(f"=========================================================================================")
    print(f"| product ID\t|  Name                      |  Price\t |  Stock\t |  Active \t|")
    print(f"|===============|============================|===========|===============|==============|")


def print_products(products_list: list[dict])-> None:
    print_products_header()
    if not products_list:
        print("\nNo results!\n")
        return
    
    for p in products_list:
        print_product(p)
    print(f"=========================================================================================")


def product_deleted(value: bool)-> None:
    print(f"Product deleted: {value}")


if __name__ == "__main__":
    print_products(test)