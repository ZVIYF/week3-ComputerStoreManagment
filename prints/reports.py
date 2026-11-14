def print_header(title:str=""):
    print()
    print(f"=========== {title} ===========")
    print()


def print_next_rated(index, products_list: list):
    try:
        key, units = next(products_list)
        print(f"{index}. {key}: {units}")
    except StopIteration:
        print(f"{index}. None")


def report_printer(key:str, value:int|float):
    print(f"Sales {key}: {value}")
