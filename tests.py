import unittest
from pathlib import Path
from os.path import join
from os import (
    environ,
    remove
)

from utils.environment_variables import (
    set_environment_variables,
    set_files_destination
)


class TestEnvironmentVariablesModule(unittest.TestCase):

    test_base_dir = None
    test_environment_file_name = '.test_env_file'

    @classmethod
    def setUpClass(cls):
        cls.test_base_dir = Path(__file__).parent.absolute()
        cls.create_test_environment_file(cls, cls.test_base_dir)

    def create_test_environment_file(self, path):
        with open(join(path, self.test_environment_file_name), 'w') as f:
            f.write(
                'PROJECT=FOLDERS_ORGANIZER\nDUMMY_VAR=DUMMY\n'
                'FOLDER_FOR_DUMMY=DUMMY_FOLDER\n'
                'EXTENSIONS_FOR_DUMMY_FOLDER=.txt'
            )

    def test_set_environment_variables(self):
        set_environment_variables(
            join(
                self.test_base_dir,
                self.test_environment_file_name
            )
        )
        project_name = environ.get('PROJECT')
        dummy_var = environ.get('DUMMY_VAR')
        dummy_folder = environ.get('FOLDER_FOR_DUMMY')
        self.assertEqual(project_name, 'FOLDERS_ORGANIZER')
        self.assertEqual(dummy_var, 'DUMMY')
        self.assertEqual(dummy_folder, 'DUMMY_FOLDER')

    def test_set_files_destination(self):
        files_destination = set_files_destination()
        self.assertEqual(files_destination['DUMMY_FOLDER'], ['.txt'])

    @classmethod
    def tearDownClass(cls):
        remove(join(cls.test_base_dir, cls.test_environment_file_name))


if __name__ == '__main__':
    unittest.main()
