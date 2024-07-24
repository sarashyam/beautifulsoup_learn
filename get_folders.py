import os

directory_path = r'C:\Users'

folders = [f for f in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, f))]

print(folders)

username = ""
for folder_name in folders:
    if folder_name.startswith("user"):
        username = folder_name
print(username)