import os

from docs import config
from organizer.system_handler import SystemHandler

FILES_DESTINATION = {
    'images': ['.jpg', '.jpeg', '.png'],
    'documents': ['.pdf', '.xlsx', '.docx', '.txt'],
}
FOLDER_TO_ORGANIZE = config.FOLDER_TO_ORGANIZE_TEST

handler = SystemHandler(
    folder_to_organize=FOLDER_TO_ORGANIZE,
    files_handler=FILES_DESTINATION
)


def test_get_folders_to_create():
    assert handler.get_folders_to_create() == ['images', 'documents', 'others']


def test_get_file_from_full_path():
    full_path_to_file = '/User/Documents/test.txt'
    assert handler.get_file_from_full_path(full_path_to_file) == 'test.txt'


def test_rename_file():
    file_to_rename = 'test_file.txt'
    filename = file_to_rename.split('.')[0]
    assert f'{filename}_copy_' in handler.rename_file(file_to_rename)


def test_get_destination_by_extension():
    file_to_organize = 'test_file.txt'
    destination = handler.get_destination_by_extension(file_to_organize)
    assert destination == os.path.join(
        FOLDER_TO_ORGANIZE,
        'documents',
        file_to_organize
    )
    file_to_organize = 'test_file.random_extension'
    destination = handler.get_destination_by_extension(file_to_organize)
    assert destination == os.path.join(
        FOLDER_TO_ORGANIZE,
        'others',
        file_to_organize
    )


def test_clean_file_list():
    files_to_clean = ['test.txt', 'test.jpg', '.secret', 'log.txt']
    cleaned_files = handler.clean_file_list(files_to_clean)
    assert cleaned_files == ['test.txt', 'test.jpg']
