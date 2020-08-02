from os import (
    listdir,
    environ,
    mkdir,
    rename
)
from os.path import (
    isfile,
    isdir,
    join,
    splitext
)
from pathlib import Path

from environment_variables import set_environment_variables

BASE_DIR = Path(__file__).parent.absolute()
ENVIRONMENT_FILE = join(BASE_DIR, '.env')

set_environment_variables(
    join(BASE_DIR, '.env')
)

path = environ.get('FOLDER_TO_ORGANIZE')

files_to_organize = [
    f for f in listdir(path) if isfile(join(path, f))
]

folders_to_check = environ.get('FOLDERS').split(',')
for folder in folders_to_check:
    if not isdir(join(path, folder)):
        mkdir(join(path, folder))

current_folders = [
    f for f in listdir(path) if isdir(join(path, f))
]

FILES_DESTINATION = {
    '.jpg': 'images',
    '.png': 'images',
    '.pdf': 'documents',
    '.xlsx': 'documents',
    '.zip': 'compressed',
    '.rar': 'compressed',
    '.pkg': 'apps',
    '.dmg': 'apps',
    'py': 'scripts',
    '.mp3': 'audios',
    '.mp4': 'videos',
    '.flv': 'videos'
}

for full_filename in files_to_organize:
    source = join(path, full_filename)

    filename, extension = splitext(full_filename)

    if extension.lower() in FILES_DESTINATION.keys():
        destination = join(
            path,
            FILES_DESTINATION[extension.lower()],
            full_filename
        )
    else:
        destination = join(
            path,
            environ.get('FOLDER_FOR_OTHERS'),
            full_filename
        )

    rename(source, destination)
