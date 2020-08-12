[![Coverage Status](https://coveralls.io/repos/github/jalvaradosegura/folder_organizer/badge.svg?branch=master)](https://coveralls.io/github/jalvaradosegura/folder_organizer?branch=master)

# Folder Organizer 🗂
Automation to organize the files within a folder, moving them into custom folders. Schedule the execution with crontab to take it to the next level

## Watch it in action
![Example](https://media.giphy.com/media/Z9KPDEo1LetVfOyMru/giphy.gif)

## Goals
* Keep a folder cleaner
* Save time

# How to use it?
Edit the config.py file within the docs folder. There are seven variables that must be set, the first six:

```py
# Example values

# If IS_TESTING is true, the script will organize the FOLDER_TO_ORGANIZE_TEST instead of FOLDER_TO_ORGANIZE.
# The point of this is to look on a dummy folder how your current organization will look like.
# So the system will create dummy files and organize them within the test folder
IS_TESTING = True
FOLDER_TO_ORGANIZE_TEST = '/Users/test_user/Downloads/test_folder'

# Folder to organize
FOLDER_TO_ORGANIZE = '/Users/test_user/Downloads'

# If there is a file within the FOLDER_TO_ORGANIZE that does not match up any known extension, 
# that file will go under this folder.
FOLDER_FOR_OTHERS = 'others'

# All the files movements that the script makes, will be stored within this file.
LOG_FILE = '/Users/test_user/Downloads/log.txt'

# If true, the script will ignore files that their name starts with a period
IGNORE_HIDDEN_FILES = True
```

>💡 File routes need to be the absolute path

Currently, the only way of organization available is by file extension.
You need to set the FILES_DESTINATION variable in order to tell the script how to organize your files.
This variable must be a dictionary, and its keys will be the name of the folder and the values the extensions that will go into that folder.
For example:

```py
# Example values
FILES_DESTINATION = {
    'images': ['.jpg', '.jpeg', '.png'],
    'documents': ['.pdf', '.xlsx', '.docx', '.txt'],
    'apps': ['.pkg', '.dmg', '.exe'],
    'videos': ['.mp4', '.flv'],
    'audios': ['.mp3'],
    'compressions': ['.rar', '.zip'],
    'scripts': ['.py', '.rb', '.js', '.html'],
}
```
>💡 Yes, you have to add the extensions with the period

Finally run the main.py to organize your desired folder

## Crontanb
Add the execution of the main.py script to crontab, so your desired folder gets organized every so often.

Open crontab.

```sh
crontab -e
```

Add this line at the end of the file to execute the script every 30 minutes:
```sh
*/30 * * * * python3 /Users/test_user/Documents/folders_organizer/main.py
```
Save it and you will have your desired folder organized most of the time 😁

>💡 You have to grant system access to crontab in order for the script to work
