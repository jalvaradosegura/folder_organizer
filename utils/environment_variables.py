import os


def set_environment_variables(environment_file='.env'):
    with open(environment_file) as f:
        for var in f.readlines():
            if '=' in var and not var.startswith('#'):
                print(var)
                key, value = var.replace('\n', '').split('=')
                os.environ[key] = value
