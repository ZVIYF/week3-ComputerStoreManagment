from DB.categories import CATEGORIES
from utils.categories import return_categories_list


def valid_product_category(category: str):
    if not category.lower() in CATEGORIES:
        raise ValueError(f"Category must be in the categories list:\n {return_categories_list(CATEGORIES)}")


def valid_ID(search_result: list):
    if not search_result:
            raise ValueError("Product ID does not exists")