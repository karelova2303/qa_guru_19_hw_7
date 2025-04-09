import os
import zipfile

import pytest


# Фикстура для создания архива из файлов
@pytest.fixture
def create_archive():
    file_names = ['Test_CSV.csv',
                  'Test_Excel.xlsx',
                  'Test_Pdf.pdf']
    dir_path = os.getcwd()
    file_path = os.path.join(dir_path, 'files')

    if not os.path.exists(os.path.join(dir_path, 'resources')):
        os.mkdir(os.path.join(dir_path, 'resources'))
    with zipfile.ZipFile(os.path.join(dir_path, 'resources', 'archive_files.zip'), 'w') as zf:
        for file in file_names:
            add_file = os.path.join(file_path, file)
            zf.write(add_file, os.path.basename(add_file))

