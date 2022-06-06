from msilib.schema import Error
from zipfile import ZipFile
from utils.logging import log_backup
from models.enums import log_backup_options

def show_options():
    print("\nPress 1 to create a backup")
    print("Press 2 to restore a backup")
    print("Press 3 to go back")

    while True:
        user_option = input("\nEnter your option: ")

        # Create backup
        if user_option == "1":
            create_backup()
            return

        # Restore backup
        elif user_option == "2":
            restore_backup()
            return

        # Go back to previous page (main page)
        elif user_option == "3":
            return

        else: 
            print("Incorrect input, please try again")
            continue

def create_backup():
    # Creates the backup.zip file if it doesn't exist yet, and if it exists, overwrites everything that's in the zip
    with ZipFile('backup.zip', 'w') as backup_zip:
        # Adds the database to the backup zip
        backup_zip.write('pythonsqlite.db')
    
    # Logs the backup creation
    log_backup(log_backup_options.CREATION)

    print("Backup has been successfully made")

def restore_backup():
    try:
        # Extracts the database file and overwrites it
        with ZipFile('backup.zip', 'r') as backup_zip:
            backup_zip.extractall()

        # Logs the backup restoration
        log_backup(log_backup_options.RESTORATION)

        print("Backup has been successfully restored")

    except Exception as exc:
        print(f"Restoring from backup failed.\nError: {exc}")