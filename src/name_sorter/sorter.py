from name_sorter.name import Name

def sort_names(names: list[Name]) -> list[Name]:
    # Efficiently sort names by key using the `sort_key` property of the `Name` class
    # and Python's built-in `sorted` function, which is stable and efficient
    return sorted(names, key=lambda name: name.sort_key)
