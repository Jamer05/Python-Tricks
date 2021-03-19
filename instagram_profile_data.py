#if you are using google collab "!pip install bs4" && "!pip install requests"

from bs4 import BeautifulSoup
import requests
URL = 'https://www.instagram.com/{}/'
 
def scrap_data(user_name):
    data = requests.get(URL.format(user_name))
    soup = BeautifulSoup(data.text,'html.parser')
    meta = soup.find('meta',property='og:description')
    s = meta.attrs['content']
    s = s.split('-')[0]
    print(s)
 
if __name__ == '__main__':
    user_name = 'dynamic.coding'
    scrap_data(user_name)
 