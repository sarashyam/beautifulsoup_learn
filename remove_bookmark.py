# import json
# import os

# # Path to the Chrome bookmark file (adjust according to your OS)
# bookmark_file_path = os.path.expanduser('~') + '/AppData/Local/Google/Chrome/User Data/Default/Bookmarks'

# def remove_bookmark(bookmark_file, bookmark_name):
#     with open(bookmark_file, 'r', encoding='utf-8') as file:
#         bookmarks = json.load(file)

#     def remove_bookmark_from_folder(folder):
#         to_remove = []
#         for i, bookmark in enumerate(folder.get('children', [])):
#             if bookmark['type'] == 'folder':
#                 remove_bookmark_from_folder(bookmark)
#             elif bookmark['type'] == 'url' and bookmark['name'] == bookmark_name:
#                 to_remove.append(i)
        
#         for i in reversed(to_remove):
#             del folder['children'][i]

#     remove_bookmark_from_folder(bookmarks['roots']['bookmark_bar'])
#     remove_bookmark_from_folder(bookmarks['roots']['other'])

#     with open(bookmark_file, 'w', encoding='utf-8') as file:
#         json.dump(bookmarks, file, indent=4)

# # Example usage
# remove_bookmark(bookmark_file_path, 'Example Bookmark Name')

import json
import os

bookmark_file_path= r'C:\Users\user105\AppData\Local\Google\Chrome\User Data\Default\Bookmarks'

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