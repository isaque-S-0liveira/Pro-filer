from datetime import datetime
from pro_filer.actions.main_actions import show_details  # NOQA


def create_temp_file(path):
    with open(path, "w", encoding="utf-8"):
        pass


def test_show_details(capsys, tmp_path):
    temp_file = tmp_path / "Trybe_logo.png"
    create_temp_file(temp_file)
    context = {"base_path": str(temp_file)}

    expect_output = (
        "File name: Trybe_logo.png\n"
        "File size in bytes: 0\n"
        "File type: file\n"
        "File extension: .png\n"
        f"Last modified date: {datetime.now().strftime('%Y-%m-%d')}\n"
    )
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == expect_output
