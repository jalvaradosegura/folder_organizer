from docs import config
from organizer.system_handler import SystemHandler

FILES_DESTINATION = {
    'images': ['.jpg', '.jpeg', '.png'],
    'documents': ['.pdf', '.xlsx', '.docx', '.txt'],
}


def test_get_folders_to_create():
    handler = SystemHandler(
        folder_to_organize=config.FOLDER_TO_ORGANIZE_TEST,
        files_handler=FILES_DESTINATION
    )
    assert handler.get_folders_to_create() == ['images', 'documents', 'others']
