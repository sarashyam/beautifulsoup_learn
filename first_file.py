# import requests
from bs4 import BeautifulSoup

# url = 'https://en.wikipedia.org/wiki/HTML'

# r = requests.get(url)
# print(r.text)
# with open('sample.html','w') as f:
#     f.write(r.text)

import requests

url = 'https://outlook.office.com/mail/inbox/id/AAMkAGNhOWMwOWEyLTkxZmQtNDQxMS05MGViLWNiNmEzZjBiZjJiMgBGAAAAAACvzg4dtQo3SaKFmq5WjzGOBwAh4Sequ5G4S6LJCI%2FWhO0UAAAAAAEMAAAh4Sequ5G4S6LJCI%2FWhO0UAADDTVMrAAA%3D'

# Make the HTTP request
r = requests.get(url)

# Check if the request was successful
if r.status_code == 200:
    # Open the file in write mode and ensure the correct encoding
    with open('sample1.html', 'w', encoding='utf-8') as f:
        f.write(r.text)
else:
    print(f"Failed to retrieve the page. Status code: {r.status_code}")

with open('sample1.html','r', encoding='utf-8') as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc,'html.parser')
print(soup.prettify())
p = soup.prettify()
with open('sample1.html', 'w', encoding='utf-8') as f:
        f.write(p)
# # print(soup.title) # <title>HTML - Wikipedia</title>
# # print(soup.title.name) # title
# # print(soup.title.string) # HTML - Wikipedia

# # print(soup.div)
# # print(soup.find_all('div')[0])

# for link in soup.find_all('a'):
#     print(link.get('href'))
    
# print(soup.find(class_= 'vector-dropdown-content'))
# print("-----------------------------------------------------------------------")   
# # to find the children of class 'vector-dropdown-content'
# for child in soup.find(class_="vector-dropdown-content").children:
#     print(child)
# print("-----------------------------------------------------------------------")   

# # to find the parent of the class 'vector-dropdown-content'
# for parent in soup.find(class_ = 'vector-dropdown-content').parents:
#     print(parent)
# print("-----------------------------------------------------------------------")   