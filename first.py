import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)
# print(response.status_code)
# print(response.text)

page_html = response.text

soup = BeautifulSoup(page_html, features = 'html.parser')
print(soup.prettify())