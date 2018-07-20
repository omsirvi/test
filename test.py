import requests
from bs4 import BeautifulSoup

def run():
    page = requests.get('http://www.ecourts.gov.in/ecourts_home/')
    soup = BeautifulSoup(page.text, 'html.parser')
    print(soup.get_text())
    fileopen = open('index.html', 'w' )
    fileopen.write(soup.get_text())
    fileopen.close()
run()

