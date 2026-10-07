import pytest

from name_sorter.name import Name


def test_from_string_parses_name():
    name = Name.from_string("Adonis Julius Archer")

    assert name.given_names == ("Adonis", "Julius")
    assert name.last_name == "Archer"


def test_from_string_accepts_one_given_name():
    name = Name.from_string("Janet Parsons")

    assert name.given_names == ("Janet",)
    assert name.last_name == "Parsons"


def test_from_string_accepts_three_given_names():
    name = Name.from_string("John Michael David Smith")

    assert name.given_names == ("John", "Michael", "David")
    assert name.last_name == "Smith"


@pytest.mark.parametrize(
    "value",
    [
        "Smith",
        "John Michael David James Smith",
    ],
)
def test_from_string_rejects_invalid_number_of_given_names(value):
    with pytest.raises(ValueError):
        Name.from_string(value)


def test_string_representation_preserves_full_name():
    name = Name(
        given_names=("Adonis", "Julius"),
        last_name="Archer",
    )

    assert str(name) == "Adonis Julius Archer"
