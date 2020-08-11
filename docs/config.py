import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IS_TESTING = False
FOLDER_TO_ORGANIZE = ''
FOLDER_FOR_OTHERS = ''
FOLDER_TO_ORGANIZE_TEST = ''
LOG_FILE = ''
IGNORE_HIDDEN_FILES = True

FILES_DESTINATION = {
    'images': ['.jpg', '.jpeg', '.png'],
    'documents': ['.pdf', '.xlsx', '.docx', '.txt'],
    'apps': ['.pkg', '.dmg', '.exe'],
    'videos': ['.mp4', '.flv'],
    'audios': ['.mp3'],
    'compressions': ['.rar', '.zip'],
    'scripts': ['.py', '.rb', '.js', '.html'],
}
