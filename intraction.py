import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup

url = "https://edunetfoundation.org/"
response = requests.get(url)

# check if the request is successful
if response.status_code ==  500:
    print("Successfully fethed the web page")
else:
    print("Failed")


# #check if the request is successful
if response.status_code == 200:
    print("Successfully fetched the web page")
else:
    print("Failed")

soup=BeautifulSoup(response.text,"html.parser")

title=soup.title.string
print(f"Page Title:{title}:")



links=soup.find_all("a")
for link in links:
    href =link.get("href")
    text= link.get_text()
    print(f"link text : {text},URL:{href}")

response=requests.get(url)

check if the request is successful
if response.status_code == 200:
    print("Successfully fethed the web page")
else:
    print("Failed")


# #check if the request is successful
if response.status_code == 200:
    print("Successfully fetched the web page")
else:
    print("Failed")

soup=BeautifulSoup(response.text,"html.parser")

title=soup.title.string
print(f"Page Title:{title}:")



links=soup.find_all("a")
for link in links:
    href =link.get("href")
    text= link.get_text()
    print(f"link text : {text},URL:{href}")


import csv
links=soup.find_all("a")
with open("website_links.csv", "w",newline="",encoding="utf-8") as file
     writer=csv.writer(file)


#
import requests
from bs4 import BeautifulSoup

url="https://www.amazon.com/"
response=requests.get(url)


soup=BeautifulSoup(response.text,"html.parser")


title=soup.title.string
print(f"Page title: {title}")




import csv

links=soup.find_all("a")

with open("website_links.csv","w",newline="",encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Link Text", "URL"])

    for link in links:
        href=link.get("href")
        text=link.get_text(strip=True)
        writer.writerow([text,href])

        print("Link saved successfully")
