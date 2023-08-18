from datetime import datetime
import os
from pro_filer.actions.main_actions import show_details  # NOQA


def create_temp_file(path):
    with open(path, "w", encoding="utf-8"):
        pass


def test_show_details_extension(capsys, tmp_path):
    temp_file = tmp_path / "Trybe_logo.png"
    create_temp_file(temp_file)
    context = {"base_path": str(temp_file)}

    expect_output = (
        "File name: Trybe_logo.png\n"
        f"File size in bytes: {os.path.getsize(temp_file)}\n"
        "File type: file\n"
        "File extension: .png\n"
        f"Last modified date: {datetime.now().strftime('%Y-%m-%d')}\n"
    )
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == expect_output


def test_show_details_no_extension(capsys, tmp_path):
    temp_dir = tmp_path / "Trybe_test"
    temp_dir.mkdir()  # Cria o diretório temporário
    context = {"base_path": str(temp_dir)}

    expect_output = (
        "File name: Trybe_test\n"
        f"File size in bytes: {os.path.getsize(temp_dir)}\n"
        "File type: directory\n"
        "File extension: [no extension]\n"
        f"Last modified date: {datetime.now().strftime('%Y-%m-%d')}\n"
    )
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == expect_output


def test_show_details_file_not_exist(capsys):
    context = {"base_path": "path_invalido"}
    expect_output = "File 'path_invalido' does not exist\n"
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == expect_output
