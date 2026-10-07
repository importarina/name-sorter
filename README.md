# Name Sorter

Sort a file of names by last name, then by given names. Each name must contain
one to three given names followed by a last name, with one name per line.

## Install and run

```sh
python -m pip install .
name-sorter ./unsorted-names-list.txt
```

The sorted names are printed to the screen and written to
`sorted-names-list.txt` in the current working directory.

## Run tests

```sh
python -m pip install ".[test]"
python -m pytest
```
