import os

from organizer.system_handler import SystemHandler
from organizer.logger import Logger

FILES_DESTINATION = {
    'images': ['.jpg', '.jpeg', '.png'],
    'documents': ['.pdf', '.xlsx', '.docx', '.txt'],
}
FOLDER_TO_ORGANIZE = 'dir_for_testing'

handler = SystemHandler(
    folder_to_organize=FOLDER_TO_ORGANIZE,
    files_handler=FILES_DESTINATION
)
handler.logger.file_to_write_in = os.path.join(FOLDER_TO_ORGANIZE, 'log.txt')


def delete_directory(directory):
    for item in os.listdir(directory):
        filename = os.path.join(directory, item)
        if os.path.isfile(filename):
            os.remove(filename)
            continue
        folder = os.path.join(directory, item)
        for item in os.listdir(folder):
            filename = os.path.join(folder, item)
            os.remove(filename)
        os.rmdir(folder)
    os.rmdir(directory)


def setup_function(function):
    os.mkdir(FOLDER_TO_ORGANIZE)
    os.mkdir(f'{FOLDER_TO_ORGANIZE}/images')
    with open(f'{FOLDER_TO_ORGANIZE}/picture.jpg', 'w'):
        pass
    with open(f'{FOLDER_TO_ORGANIZE}/unknown_file.unknown_extension', 'w'):
        pass


def teardown_function(function):
    delete_directory(FOLDER_TO_ORGANIZE)


def test_get_folders_to_create():
    assert handler.get_folders_to_create() == ['images', 'documents', 'others']


def test_create_folders():
    handler.create_folders()
    assert os.listdir(FOLDER_TO_ORGANIZE) == [
        'unknown_file.unknown_extension', 'images',
        'others', 'documents', 'picture.jpg'
    ]


def test_get_files_in_folder_to_organize():
    assert handler.get_files_in_folder_to_organize() == [
        'unknown_file.unknown_extension', 'picture.jpg'
    ]


def test_get_file_from_full_path():
    full_path_to_file = '/User/Documents/test.txt'
    assert handler.get_file_from_full_path(full_path_to_file) == 'test.txt'


def test_rename_file():
    file_to_rename = 'test_file.txt'
    filename = file_to_rename.split('.')[0]
    assert f'{filename}_copy_' in handler.rename_file(file_to_rename)


def test_move_file():
    file_to_move = os.path.join(FOLDER_TO_ORGANIZE, 'picture.jpg')
    file_destination = os.path.join(FOLDER_TO_ORGANIZE, 'images', 'picture.jpg')
    handler.move_file(file_to_move, file_destination)
    assert os.listdir(os.path.join(FOLDER_TO_ORGANIZE, 'images')) == ['picture.jpg']


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


def test_organize():
    handler.organize()
    folder_for_others = os.path.join(FOLDER_TO_ORGANIZE, 'others')
    folder_for_images = os.path.join(FOLDER_TO_ORGANIZE, 'images')

    assert os.listdir(FOLDER_TO_ORGANIZE) == [
        'images', 'others', 'log.txt', 'documents'
    ]
    assert os.listdir(folder_for_others) == ['unknown_file.unknown_extension']
    assert os.listdir(folder_for_images) == ['picture.jpg']


def test_log_to_file():
    logger = Logger()
    log_file = os.path.join(FOLDER_TO_ORGANIZE, 'log.txt')
    logger.file_to_write_in = log_file
    logger.log_to_file('This is a test')
    with open(log_file) as f:
        assert 'This is a test' in f.readline()
