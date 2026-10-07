from name_sorter.name import Name
from name_sorter.sorter import sort_names


def test_sort_names_sorts_by_last_name():
    names = [
        Name.from_string("Janet Parsons"),
        Name.from_string("Hunter Uriah Mathew Clarke"),
        Name.from_string("Adonis Julius Archer"),
    ]

    result = sort_names(names)

    assert [str(name) for name in result] == [
        "Adonis Julius Archer",
        "Hunter Uriah Mathew Clarke",
        "Janet Parsons",
    ]


def test_sort_names_sorts_by_given_names_when_last_names_match():
    names = [
        Name.from_string("Zoe Smith"),
        Name.from_string("Alice Zoe Smith"),
        Name.from_string("Alice Bob Smith"),
    ]

    result = sort_names(names)

    assert [str(name) for name in result] == [
        "Alice Bob Smith",
        "Alice Zoe Smith",
        "Zoe Smith",
    ]


def test_sort_names_does_not_modify_input_list():
    names = [
        Name.from_string("Zoe Smith"),
        Name.from_string("Alice Brown"),
    ]
    original = names.copy()

    sort_names(names)

    assert names == original
