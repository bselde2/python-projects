import os 
import shutil
import datetime
import schedule 
import time

source_dir = "/home/dev-bryce/Documents/vs code python projects"
destination_dir = "/home/dev-bryce/Documents/Backups"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exist in: {dest}")   


schedule.every().day.at("18:28").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)

