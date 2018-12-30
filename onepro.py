import requests
from bs4 import BeautifulSoup
url = requests.get('https://www.radiojavan.com/mp3s')
print(url)
