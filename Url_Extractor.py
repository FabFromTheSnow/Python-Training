import requests
import re
from bs4 import BeautifulSoup

url = input("Enter the url: ")

if url.startswith("www."):
    url = "https://" + url
elif not url.startswith("https://www."):
    url = "https://www." + url

page = requests.get(url)

oui = str(BeautifulSoup(page.content, 'html.parser'))
urls = re.findall('(https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[^\s)\(\"",;*\']*)', oui) #Thanks GPT for the regex <3

with open('link.txt', "w") as file:
    for url in urls:
        file.write(url + '\n')

print("link availalble in link.txt")
