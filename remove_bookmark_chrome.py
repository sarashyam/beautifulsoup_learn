'''
History
2024-07-23 SAS - to remove all the bookmarks in the chrome
2024-07-23 SAS - take username from the c folder
'''
import json
import os

directory_path = r'C:\Users'

folders = [f for f in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, f))]

print(folders)

username = ""
for folder_name in folders:
    if folder_name.startswith("user"):
        username = folder_name
print(username)


bookmark_file_path= fr'C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Bookmarks'

def remove_all_bookmarks(bookmark_file):
    # Read the bookmark file
    with open(bookmark_file, 'r', encoding='utf-8') as file:
        bookmarks = json.load(file)

    # Clear the 'children' list for 'bookmark_bar' and 'other' folders
    bookmarks['roots']['bookmark_bar']['children'] = []
    bookmarks['roots']['other']['children'] = []

    # Write the modified bookmarks back to the file
    with open(bookmark_file, 'w', encoding='utf-8') as file:
        json.dump(bookmarks, file, indent=4)

# Remove all bookmarks
remove_all_bookmarks(bookmark_file_path)