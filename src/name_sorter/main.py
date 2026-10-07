import sys
from name_sorter.name import Name
from name_sorter.sorter import sort_names

OUTPUT_FILE = "sorted-names-list.txt"

def main():
    input_path = sys.argv[1]
    with open(input_path, encoding="utf-8") as file:
        # Turn the lines in the file into names and validate
        names = [Name.from_string(line) for line in file if line.strip()]

    # Sort the names
    names = sort_names(names)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as output_file:

        for name in names:
            print(name)
            output_file.write(f"{name}\n")


if __name__ == "__main__":
    main()
