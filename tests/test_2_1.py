import os

import pytest

from main.task_2_1 import create_file


@pytest.fixture(scope="module")
def create_and_cleanup_files():
    filenames = [f"file_{i}.txt" for i in range(10)]
    yield filenames
    for filename in filenames:
        if os.path.exists(filename):
            os.remove(filename)


def test_create_file(create_and_cleanup_files):
    assert create_file(1) == 'file_1.txt'


def test_name_and_content_files(create_and_cleanup_files):
    assert os.path.exists('file_1.txt'), f"Файл {'file_1.txt'} не был создан."
    with open('file_1.txt', 'r') as file:
        content = file.read()
        assert content == str(1), f"Содержимое файла {'file_1.txt'} неверно."


if __name__ == '__main__':
    pytest.main()