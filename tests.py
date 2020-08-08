import unittest
from pathlib import Path
from os.path import (
    join,
    isdir
)
from os import (
    environ,
    remove,
    rmdir
)

from utils.environment_variables import (
    set_environment_variables,
    set_files_destination
)
from utils.system_handler import SystemHandler

BASE_DIR = Path(__file__).parent.absolute()


class TestApp(unittest.TestCase):

    test_environment_file_name = '.test_env_file'

    @classmethod
    def setUpClass(cls):
        cls.create_test_environment_file(cls, BASE_DIR)
        set_environment_variables(
            join(
                BASE_DIR,
                cls.test_environment_file_name
            )
        )
        cls.files_handler = set_files_destination()
        cls.system_handler = SystemHandler(BASE_DIR, cls.files_handler)

    def create_test_environment_file(self, path):
        with open(join(path, self.test_environment_file_name), 'w') as f:
            text_for_file = (f"FOLDER_TO_ORGANIZE={BASE_DIR}\n"
                             "FOLDER_FOR_OTHERS=others\n"
                             "FOLDER_FOR_IMAGES=images\n"
                             "EXTENSIONS_FOR_IMAGES=.jpg,.png\n")
            f.write(text_for_file)

    def test_set_environment_variables(self):
        folder_to_organize = environ.get('FOLDER_TO_ORGANIZE')
        folder_for_others = environ.get('FOLDER_FOR_OTHERS')
        self.assertEqual(folder_to_organize, str(BASE_DIR))
        self.assertEqual(folder_for_others, 'others')

    def test_set_files_destination(self):
        self.assertEqual(self.files_handler['images'], ['.jpg', '.png'])

    def test_get_folders(self):
        folders = self.system_handler.get_folders()
        self.assertEqual(folders, ['others', 'images'])

    def test_get_files(self):
        files = self.system_handler.get_files()
        self.assertTrue(__file__ in files)

    def test_create_folders(self):
        self.system_handler.create_folders()
        self.assertTrue(isdir(join(BASE_DIR, 'others')))
        self.assertTrue(isdir(join(BASE_DIR, 'images')))

    @classmethod
    def tearDownClass(cls):
        remove(join(BASE_DIR, cls.test_environment_file_name))
        rmdir(join(BASE_DIR, 'others'))
        rmdir(join(BASE_DIR, 'images'))


if __name__ == '__main__':
    unittest.main()
