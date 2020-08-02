from os import environ
from os.path import join
from pathlib import Path

from utils.environment_variables import (
    set_environment_variables,
    set_files_destination
)
from utils.system_handler import SystemHandler
from utils.files_factory import files_factory


if __name__ == '__main__':

    PROJECT_BASE_DIR = Path(__file__).parent.absolute()
    ENVIRONMENT_FILE = join(PROJECT_BASE_DIR, '.env')
    set_environment_variables(
        join(PROJECT_BASE_DIR, '.env')
    )

    FILES_DESTINATION = set_files_destination()
    path = environ.get('FOLDER_TO_ORGANIZE')

    if environ.get('IS_TESTING') == '1':
        path = environ.get('FOLDER_TO_ORGANIZE_TEST')
        files_factory(path, FILES_DESTINATION)

    handler = SystemHandler(path, FILES_DESTINATION)
    handler.create_folders()
    handler.organize()
