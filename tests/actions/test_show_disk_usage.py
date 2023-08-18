from pro_filer.actions.main_actions import show_disk_usage  # NOQA


def create_temp_file1(path):
    with open(path, "w", encoding="utf-8") as file:
        file.write(":)")


def create_temp_file2(path):
    with open(path, "w", encoding="utf-8") as file:
        file.write("<:)")


def test_show_disk_usage(capsys, tmp_path):
    tmp_file_1 = tmp_path / "file_1"
    tmp_file_2 = tmp_path / "file_2"

    create_temp_file1(tmp_file_1)
    create_temp_file2(tmp_file_2)

    # Crie os caminhos absolutos completos
    abs_tmp_file_1 = str(tmp_file_1)
    abs_tmp_file_2 = str(tmp_file_2)

    context = {
        "all_files": [
            abs_tmp_file_1,
            abs_tmp_file_2,
        ]
    }
    expect_output = (
        f"'{abs_tmp_file_2}':        3 (60%)\n"
        f"'{abs_tmp_file_1}':        2 (40%)\n"
        "Total size: 5\n"
    )
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == expect_output


def test_show_disk_usage_empty(capsys):
    context = {"all_files": []}
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == "Total size: 0\n"
