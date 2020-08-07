import os


def set_environment_variables(environment_file='.env'):
    assert os.path.isfile(environment_file), 'File for environment variables' \
                                             ' does not exist'
    with open(environment_file) as f:
        for var in f.readlines():
            if '=' in var and not var.startswith('#'):
                key, value = var.replace('\n', '').split('=')
                os.environ[key] = value


def set_files_destination():
    files_destination = {}
    for key, value in os.environ.items():
        if ('FOLDER_FOR_' in key
                and 'FOLDER_FOR_OTHERS' not in key
                and 'FOLDER_TO_ORGANIZE' not in key):
            extensions_as_string = os.environ.get(
                f'EXTENSIONS_FOR_{value.upper()}'
            )
            extensions_as_list = extensions_as_string.split(',')
            files_destination[value] = extensions_as_list
    return files_destination
