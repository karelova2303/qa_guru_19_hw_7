import os
import zipfile

import pytest


# Фикстура для создания архива из файлов
@pytest.fixture
def create_archive():
    file_names = ['Test_CSV.csv',
                  'Test_Excel.xlsx',
                  'Test_Pdf.pdf']

    file_path = os.path.join(os.getcwd(), 'files')

    with zipfile.ZipFile('archive_files.zip', 'w') as zf:
        for file in file_names:
            add_file = os.path.join(file_path, file)
            zf.write(add_file, os.path.basename(add_file))
