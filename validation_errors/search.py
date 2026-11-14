def valid_search_key(user_input: str):
    if user_input not in ("id", "category", "name"):
        raise ValueError("Search key must be one of the following: ID/Category/Name")
    