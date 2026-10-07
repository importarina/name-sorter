import sys

from name_sorter.main import main


def test_main_prints_and_writes_sorted_names(tmp_path, monkeypatch, capsys):
    input_file = tmp_path / "unsorted-names-list.txt"
    input_file.write_text(
        "Janet Parsons\n"
        "Adonis Julius Archer\n"
        "Hunter Uriah Mathew Clarke\n",
        encoding="utf-8",
    )

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "argv", ["name-sorter", str(input_file)])

    main()

    expected = (
        "Adonis Julius Archer\n"
        "Hunter Uriah Mathew Clarke\n"
        "Janet Parsons\n"
    )

    assert capsys.readouterr().out == expected

    output_file = tmp_path / "sorted-names-list.txt"
    assert output_file.read_text(encoding="utf-8") == expected
