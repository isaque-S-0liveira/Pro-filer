from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview_with_files_and_dirs(capsys):
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
            "src/test1",
            "src/test2",
            "src/xxxxx",
        ],
        "all_dirs": ["src", "src/utils"],
    }

    show_preview(context)
    captured = capsys.readouterr()
    expected_output = (
        "Found 6 files and 2 directories\n"
        "First 5 files: ['src/__init__.py', 'src/app.py', "
        "'src/utils/__init__.py', 'src/test1', 'src/test2']\n"
        "First 5 directories: ['src', 'src/utils']\n"
    )
    assert captured.out == expected_output


def test_show_preview_with_no_files_and_dirs(capsys):
    context = {"all_files": [], "all_dirs": []}

    show_preview(context)
    captured = capsys.readouterr()
    expected_output = "Found 0 files and 0 directories\n"
    assert captured.out == expected_output
