# import requests
from bs4 import BeautifulSoup

# url = 'https://en.wikipedia.org/wiki/HTML'

# r = requests.get(url)
# print(r.text)
# with open('sample.html','w') as f:
#     f.write(r.text)

import requests

# url = 'https://en.wikipedia.org/wiki/HTML'

# # Make the HTTP request
# r = requests.get(url)

# # Check if the request was successful
# if r.status_code == 200:
#     # Open the file in write mode and ensure the correct encoding
#     with open('sample.html', 'w', encoding='utf-8') as f:
#         f.write(r.text)
# else:
#     print(f"Failed to retrieve the page. Status code: {r.status_code}")

with open('sample.html','r', encoding='utf-8') as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc,'html.parser')
# print(soup.prettify())
# print(soup.title) # <title>HTML - Wikipedia</title>
# print(soup.title.name) # title
# print(soup.title.string) # HTML - Wikipedia

print(soup.div)
print(soup.find_all('div')[0])