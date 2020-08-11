import os
from datetime import datetime

from docs import config


class Logger:
    file_to_write_in = None

    def log_to_file(self, message):

        current_time = datetime.now()
        message = f'{current_time}: {message}'

        file_to_write_in = config.LOG_FILE
        if file_to_write_in:
            if not os.path.isfile(file_to_write_in):
                with open(file_to_write_in, 'w') as f:
                    f.write(message)
            else:
                with open(file_to_write_in, 'r+') as f:
                    lines = f.readlines()
                    lines.insert(0, f'{message}\n')
                    f.seek(0)
                    f.writelines(lines)
