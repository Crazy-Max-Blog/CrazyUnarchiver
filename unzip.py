end = ".zip"

import zipfile
import glob
import os

for archive in glob.glob(f'**/*{end}', recursive=True):
    with zipfile.ZipFile(archive, 'r') as zip_file:
        zip_file.extractall()
    os.remove(archive)