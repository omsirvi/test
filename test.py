import requests
from bs4 import BeautifulSoup

def run():
    page = requests.get('http://www.ecourts.gov.in/ecourts_home/')
    soup = BeautifulSoup(page.text, 'html.parser')
    print(soup.a)
run()
