from os import environ
from os.path import join
from pathlib import Path

from utils.environment_variables import set_environment_variables
from utils.system_handler import SystemHandler
from utils.files_factory import files_factory


if __name__ == '__main__':

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
    path = environ.get('FOLDER_TO_ORGANIZE')

    if environ.get('IS_TESTING'):
        path = environ.get('FOLDER_TO_ORGANIZE_TEST')
        files_factory(path, FILES_DESTINATION)

    handler = SystemHandler(path, FILES_DESTINATION)
    handler.create_folders()
    handler.organize()
