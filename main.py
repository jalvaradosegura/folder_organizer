from docs import config
from organizer.system_handler import SystemHandler
from organizer.files_factory import files_factory

folder_to_organize = config.FOLDER_TO_ORGANIZE
files_destination = config.FILES_DESTINATION
if config.IS_TESTING:
    folder_to_organize = config.FOLDER_TO_ORGANIZE_TEST
    files_factory(folder_to_organize, files_destination)
handler = SystemHandler(
    folder_to_organize=folder_to_organize,
    files_handler=files_destination
)
handler.organize()
