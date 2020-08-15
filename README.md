[![Coverage Status](https://coveralls.io/repos/github/jalvaradosegura/folder_organizer/badge.svg)](https://coveralls.io/github/jalvaradosegura/folder_organizer)

# Folder Organizer 🗂
Automation to organize the files within a folder, moving them into custom folders. Schedule the execution with crontab to take it to the next level

## Watch it in action
![Example](https://media.giphy.com/media/Z9KPDEo1LetVfOyMru/giphy.gif)

## Goals
* Keep a folder cleaner
* Save time

# How to use it? 🤔
## Set up ⚙️
Edit the config.py file within the docs folder. There are seven variables that must be set:
1. **IS_TESTING**: Set it to True or False. If True, the script will organize the FOLDER_TO_ORGANIZE_TEST, otherwise, it will organize the FOLDER_TO_ORGANIZE.
2. **FOLDER_TO_ORGANIZE_TEST**: The folder that will be organized if IS_TESTING is True. The point of setting these variables, is to be able to look on a dummy folder how your current organization set up will look like.
3. **FOLDER_TO_ORGANIZE**: The actual folder that you want to organize. It will only be organized if IS_TESTING is False
4. **FOLDER_FOR_OTHERS**: If there is a file within the FOLDER_TO_ORGANIZE that doesn't match up any known organization set up, that file will go under this folder.
5. **LOG_FILE**: All the files movements that the script makes, will be stored within this file.
6. **IGNORE_HIDDEN_FILES**: Indicates if you want to ignore files that their name starts with a period. Set it to True or False.
7. **FILES_DESTINATION**: You need to set this variable in order to tell the script how to organize your files. This variable must be a dictionary, and its keys will be the name of the folder and the values the extensions that will go into that folder. Currently, the only way of organization available is by file extension.

### Set up example
```py
# Example values

IS_TESTING = True
FOLDER_TO_ORGANIZE_TEST = '/Users/test_user/Downloads/test_folder'

FOLDER_TO_ORGANIZE = '/Users/test_user/Downloads'
FOLDER_FOR_OTHERS = 'others'

LOG_FILE = '/Users/test_user/Downloads/log.txt'

IGNORE_HIDDEN_FILES = True

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

>💡 File routes **must** be the absolute path, with the exception of the FOLDER_FOR_OTHERS variable.
> And yes, you have to add the extensions with the period for the FILES_DESTINATION variable.

## Execute it! 🔥
Finally run the main.py file to organize your desired folder.
```sh
python main.py
```
> 💡 This was made using Python 3.8. It should work with any Python 3.x version. The packages within the Pipfile are only for testing purposes. So if you want to use the tests, install them.

## Add it to Crontanb
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

>💡 You have to grant system access to crontab in order for the script to work. In addition to this, the route must be the absolute path
