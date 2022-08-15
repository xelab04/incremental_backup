# Incremental Backup

Incremental backup program written entirely in Python3
Scans the folder for any existing files and copies those files to a backup folder. Folders can be specified in the paths.py file and is necessary before use. In order to know which files have changed, there is a csv file listing the file paths and their corresponding "last date modified".
The program will create the same file structure on the backup device. Meaning that a file being backed up from "/home/user/documents/file.txt" will then be found at "/backup_drive/home/user/documents/file.txt" making recovery of files much simpler. 

The program is still in Beta, meaning you may encounter bugs or errors during use. However, I feel that it is complete enough for public use.


Currently working on a companion script which will make recovery of files from a backup device much easier than manually copy/pasting.
Known bugs and issues:
  - Cannot copy files with ' in the names since the cp command does not appreciate it.
  - Encounters errors at locked files. A workaround is using sudo to run the Python script.
  - Copies Trash files.
  - Is not yet compatible with Windows or MacOS.
