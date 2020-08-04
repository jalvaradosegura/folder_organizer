from os.path import isfile
from os import environ
from datetime import datetime


class Logger:
    file_to_write_in = None

    def write_to_log_file(self, message):

        current_time = datetime.now()
        message = f'{current_time}: {message}'

        file_to_write_in = self.get_file_to_write_in()
        if file_to_write_in:
            if not isfile(file_to_write_in):
                with open(file_to_write_in, 'w') as f:
                    f.write(message)
            else:
                with open(file_to_write_in, 'r+') as f:
                    lines = f.readlines()
                    lines.insert(0, f'{message}\n')
                    f.seek(0)
                    f.writelines(lines)

    def get_file_to_write_in(self):
        if environ.get('LOG_FILE') is not None:
            self.file_to_write_in = environ.get('LOG_FILE')
        if self.file_to_write_in is None:
            self.file_to_write_in = 'log.txt'
        return self.file_to_write_in


log = Logger()
