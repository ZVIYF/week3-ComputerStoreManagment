def valid_amount_to_reduce(stock: int, user_request: int):
    if user_request > stock:
        raise ValueError(f"Cant execute. Only {stock} in stock:")