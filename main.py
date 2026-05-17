import os
import shutil

# Folder to organize
folder_path = "test_folder"

# File categories
file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Audio": [".mp3"]
}

def create_folders():
    for folder in file_types.keys():
        path = os.path.join(folder_path, folder)
        if not os.path.exists(path):
            os.makedirs(path)

def organize_files():
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            moved = False

            for folder, extensions in file_types.items():
                if any(file.endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(folder_path, folder, file))
                    moved = True
                    break

            if not moved:
                unknown_path = os.path.join(folder_path, "Others")
                if not os.path.exists(unknown_path):
                    os.makedirs(unknown_path)
                shutil.move(file_path, os.path.join(unknown_path, file))

    print("✅ Files organized successfully!")

create_folders()
organize_files()
