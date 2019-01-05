# music get links 
# دریافت لینک موزیک های جدید 
print('             ----------------> wellcome to linksmusic <---------------')
import requests
from bs4 import BeautifulSoup
import re
try:
    urls = 0
    url = requests.get(
        'http://www.silamusic.ir/%D9%BE%D8%B1%D8%B7%D8%B1%D9%81%D8%AF%D8%A7%D8%B1%D8%AA%D8%B1%DB%8C%D9%86-%D8%A2%D9%87%D9%86%DA%AF-%D9%87%D8%A7%DB%8C-97/')
    URL = url.text
    soup = BeautifulSoup(URL, 'lxml')
    links = soup.find_all('a',  href=True)
    for  a in links:
        if re.findall('http.*\.mp3', a['href']):
            if a.string is None:
                continue
            urls = urls + 1
            print('URL :', urls, '\n', "---------->", a['href'], '\n\n')
            # print('new url: ', a.get('href'),'\n')
        if urls > 9:
            break
except:
    print('!The problem of communicating with the Internet !', '\nPlease check your internet access')
finally:
    print('           ---------------------> done <-----------------------')
