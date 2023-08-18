from unittest.mock import patch
from pro_filer.actions.main_actions import show_disk_usage  # NOQA


def test_show_disk_usage(capsys, tmp_path):
    tmp_file_1 = tmp_path / "file_1"
    tmp_file_2 = tmp_path / "file_2"

    tmp_file_1.write_text(":)")
    tmp_file_2.write_text("<:)")

    abs_tmp_file_1 = str(tmp_file_1)
    abs_tmp_file_2 = str(tmp_file_2)

    context = {
        "all_files": [
            abs_tmp_file_1,
            abs_tmp_file_2,
        ]
    }
    expect_output = (
        f"'{abs_tmp_file_2}': {' ' * 8}3 (60%)\n"
        f"'{abs_tmp_file_1}': {' ' * 8}2 (40%)\n"
        "Total size: 5\n"
    )
    # show_disk_usage(context)
    with patch(
        "pro_filer.actions.main_actions._get_printable_file_path",
        lambda x: x,
    ):
        show_disk_usage(context)  # Substitua por sua função que faz print

    captured = capsys.readouterr()
    assert captured.out == expect_output


def test_show_disk_usage_empty(capsys):
    context = {"all_files": []}
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == "Total size: 0\n"
