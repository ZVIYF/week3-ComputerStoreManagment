def valid_to_add(product_id: int, sale: dict):
    for item in sale["items"]:
        if item["product_id"] == product_id:
            raise ValueError("Product already in sale. update quantity instead.")


def valid_to_change(product_id: int, sale: dict):
    for item in sale["items"]:
        if item["product_id"] == product_id:
            return
    raise ValueError("Product is not found in this sale. Add item instead.")
    

def valid_discount(discount: float):
    if not (0.0 <= discount <= 100.0):
        raise ValueError("discount must be between 0 - 100")


def valid_sale(sale: dict):
    if not sale["items"]:
        raise ValueError("Sale has no items. Plaese add items or cancle.")


