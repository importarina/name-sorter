from dataclasses import dataclass

@dataclass(frozen=True)  # no need for it to be mutable in this use case
class Name:
    given_names: tuple[str, ...]
    last_name: str

    @classmethod
    def from_string(cls, value: str) -> "Name":
        parts = value.split()

        # Validate the name has at least 1 given name and at most 3
        if not 2 <= len(parts) <= 4:
            raise ValueError("A name must have between 1 and 3 given names")

        return cls(
            given_names=tuple(parts[:-1]),
            last_name=parts[-1],
        )

    @property
    def sort_key(self) -> tuple[str, ...]:
        # Sort key is by last names first and by given name(s) second
        return (self.last_name, *self.given_names)

    def __str__(self) -> str:
        # Just return the `Name` in standard string format when using print statement
        return " ".join((*self.given_names, self.last_name))
