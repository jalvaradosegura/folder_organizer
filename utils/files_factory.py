from os.path import join


def files_factory(path, files_destination):
    for key, value in files_destination.items():
        with open(join(path, 'test' + value[0]), 'w'):
            pass
    with open(join(path, 'test' + '.random_extension'), 'w'):
        pass
