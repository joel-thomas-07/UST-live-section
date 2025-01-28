import os

# Path to Downloads folder
downloads_path = os.path.expanduser("~/Downloads")

if os.path.exists(downloads_path):
    print("Contents of Downloads folder:")
    for item in os.listdir(downloads_path):
        full_path = os.path.join(downloads_path, item)
        if os.path.isfile(full_path):
            print(f"{item} - File")
        elif os.path.isdir(full_path):
            print(f"{item} - Folder")
        else:
            print(f"{item} - Unknown")
else:
    print("Downloads folder does not exist.")
