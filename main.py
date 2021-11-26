import requests
from bs4 import BeautifulSoup

url = 'https://www.omgtu.ru/educational_activities/areas-of-training-implemented-in-omsk-university-in-accordance-with-gef-in/bachelor/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

internalLinks = [
    a.get('href') for a in soup.find_all('a')
    if a.get('href') and a.get('href').startswith('/')]
print(internalLinks)