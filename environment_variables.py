import os


def set_environment_variables(environment_file='.env'):
    with open(environment_file) as f:
        for var in f.readlines():
            if 'http' in var:
                key = var.split('=')[0]
                sliced_url = var.split('=')[1:]
                full_url = "=".join(sliced_url)
                os.environ[key] = full_url
                continue
            if '=' in var and not var.startswith('#'):
                key, value = var.replace('\n', '').split('=')
                os.environ[key] = value
