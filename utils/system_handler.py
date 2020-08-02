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


class SystemHandler():

    def __init__(self, path, handler):
        self.path = path
        self.handler = handler

    def get_files(self):
        return [f for f in listdir(self.path) if isfile(join(self.path, f))]

    def get_folders(self):
        return [v for k, v in environ.items() if k.startswith('FOLDER_FOR')]

    def create_folders(self):
        folders = self.get_folders()
        for folder in folders:
            full_path_to_folder = join(self.path, folder)
            if not isdir(full_path_to_folder):
                mkdir(full_path_to_folder)

    def organize(self):
        files_to_organize = self.get_files()
        for full_filename in files_to_organize:
            source = join(self.path, full_filename)
            destination = None

            filename, extension = splitext(full_filename)

            for key, value in self.handler.items():
                if extension.lower() in value:
                    destination = join(
                        self.path,
                        key,
                        full_filename
                    )
                    break
            if destination is None:
                destination = join(
                    self.path,
                    environ.get('FOLDER_FOR_OTHERS'),
                    full_filename
                )
            rename(source, destination)
