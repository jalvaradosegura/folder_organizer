import os
from datetime import datetime

from docs import config
from .logger import Logger


class SystemHandler:

    def __init__(self, folder_to_organize, files_handler):
        self.folder_to_organize = folder_to_organize
        self.files_handler = files_handler
        self.logger = Logger()
        self.logger.file_to_write_in = config.LOG_FILE

    def get_files_in_folder_to_organize(self):
        folder = self.folder_to_organize
        return [
            f for f in os.listdir(folder) if os.path.isfile(
                os.path.join(folder, f)
            )
        ]

    def get_folders_to_create(self):
        files_destination = [key for key, value in self.files_handler.items()]
        return files_destination + [config.FOLDER_FOR_OTHERS]

    def create_folders(self):
        folders_to_create = self.get_folders_to_create()
        folder_to_organize = self.folder_to_organize
        for folder in folders_to_create:
            full_path_to_folder = os.path.join(folder_to_organize, folder)
            if not os.path.isdir(full_path_to_folder):
                os.mkdir(full_path_to_folder)

    def move_file(self, file_to_move, destination):
        if os.path.isfile(destination):
            filename_with_extension = self.get_file_from_full_path(destination)
            new_filename = self.rename_file(filename_with_extension)
            destination = os.path.join(
                os.path.dirname(destination),
                new_filename
            )
        os.rename(file_to_move, destination)
        self.logger.log_to_file(f'Move {file_to_move} to {destination}')

    def rename_file(self, file_to_rename):
        filename, extension = os.path.splitext(file_to_rename)
        current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
        return f'{filename}_copy_{current_time}{extension}'

    def get_destination_by_extension(self, file_to_organize):
        filename, extension = os.path.splitext(file_to_organize)

        destination = None
        for key, values in self.files_handler.items():
            if extension.lower() in values:
                destination = os.path.join(
                    self.folder_to_organize,
                    key,
                    file_to_organize
                )
                break
        if destination is None:
            destination = os.path.join(
                self.folder_to_organize,
                config.FOLDER_FOR_OTHERS,
                file_to_organize
            )
        return destination

    def clean_file_list(self, files_to_clean):
        """
        Remove from the file list the files that shouldn't
        be moved by the system handler
        """
        log_file = self.get_file_from_full_path(config.LOG_FILE)
        ignore_hidden_files = config.IGNORE_HIDDEN_FILES

        cleaned_files = [f for f in files_to_clean if f != log_file]
        if ignore_hidden_files:
            cleaned_files = [f for f in cleaned_files if not f.startswith('.')]

        return cleaned_files

    def get_file_from_full_path(self, full_path):
        return full_path.split('/')[-1]

    def organize(self):
        self.create_folders()
        files_to_organize = self.get_files_in_folder_to_organize()
        cleaned_files = self.clean_file_list(files_to_organize)
        for filename in cleaned_files:
            destination = self.get_destination_by_extension(filename)
            file_to_move = os.path.join(self.folder_to_organize, filename)
            self.move_file(file_to_move, destination)
