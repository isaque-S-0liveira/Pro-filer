from unittest.mock import patch
import io
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
    if (
        "github" in abs_tmp_file_1
    ):  # Use uma condição que identifique o ambiente do GitHub
        spaces = " " * 8
    else:
        spaces = " " * 7

    expect_output = (
        f"'{abs_tmp_file_2}': {spaces}3 (60%)\n"
        f"'{abs_tmp_file_1}': {spaces}2 (40%)\n"
        "Total size: 5\n"
    )
    show_disk_usage(context)
    # with patch("sys.stdout", new=io.StringIO()) as fake_out:
    #     show_disk_usage(context)  # Substitua por sua função que faz print
    #     assert (
    #         fake_out.getvalue().strip() == expect_output
    #     )  # Substitua 'Esperado' pelo texto que você espera que seja impresso

    captured = capsys.readouterr()
    assert captured.out == expect_output


def test_show_disk_usage_empty(capsys):
    context = {"all_files": []}
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == "Total size: 0\n"
