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

PROJECT_BASE_DIR = Path(__file__).parent.absolute()
ENVIRONMENT_FILE = join(PROJECT_BASE_DIR, '.env')

set_environment_variables(
    join(PROJECT_BASE_DIR, '.env')
)

FILES_DESTINATION = {
    environ.get('FOLDER_FOR_IMAGES'): ['.jpg', '.png', ],
    environ.get('FOLDER_FOR_VIDEOS'): ['.mp4', '.flv', ],
    environ.get('FOLDER_FOR_AUDIOS'): ['.mp3', ],
    environ.get('FOLDER_FOR_DOCUMENTS'): ['.pdf', '.xlsx', '.docx', ],
    environ.get('FOLDER_FOR_APPS'): ['.pkg', '.dmg', '.exe', ],
    environ.get('FOLDER_FOR_COMPRESSIONS'): ['.zip', '.rar', '.tar', ],
    environ.get('FOLDER_FOR_SCRIPTS'): ['.py', '.sh', '.js', ],
}


def get_files(path):
    return [f for f in listdir(path) if isfile(join(path, f))]


def get_folders():
    return [v for k, v in environ.items() if k.startswith('FOLDER_FOR')]


def check_and_create_folder(path):
    folders = get_folders()
    for folder in folders:
        full_path_to_folder = join(path, folder)
        if not isdir(full_path_to_folder):
            mkdir(full_path_to_folder)


def files_factory(path, files_destination):
    for key, value in files_destination.items():
        with open(join(path, 'test' + value[0]), 'w'):
            pass
    with open(join(path, 'test' + '.random_extension'), 'w'):
        pass


path = environ.get('FOLDER_TO_ORGANIZE')
files_factory(path, FILES_DESTINATION)

check_and_create_folder(path)
files_to_organize = get_files(path)

for full_filename in files_to_organize:

    source = join(path, full_filename)
    destination = None

    filename, extension = splitext(full_filename)

    for key, value in FILES_DESTINATION.items():
        if extension.lower() in value:
            destination = join(
                path,
                key,
                full_filename
            )
            break
    if destination is None:
        destination = join(
            path,
            environ.get('FOLDER_FOR_OTHERS'),
            full_filename
        )
    rename(source, destination)
