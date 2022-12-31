import requests
from bs4 import BeautifulSoup

ITEMS = 100
URL = f'https://hh.ru/search/vacancy?text=python&items_on_page={ITEMS}&hhtmFrom=vacancy_search_list'
headers = {
    'Host': 'hh.ru',
    'User-Agent': 'Safari',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
  }

def extract_max_page():  
  hh_request = requests.get(URL,
    headers=headers)
  hh_soup = BeautifulSoup(hh_request.text, 'html.parser')
  
  pages = []
  
  paginator = hh_soup.find_all('span', {'class': 'pager-item-not-in-short-range'})
  
  for page in paginator:
    pages.append(int(page.find('a').text))
  return pages[-1]

def extract_hh_jobs(last_pages):
  jobs = []
  #for page in range(last_pages):
  
  result = requests.get(f'{URL}&page=0', headers=headers)
  print(result.status_code)
  #result = requests.get(f'{URL}&page={page}', headers=headers)
  
  soup = BeautifulSoup(result.text, 'html.parser')
  results = soup.find_all('div', {'class': 'vacancy-serp-item__layout'})
  
  for result in results:
    print(result.find('a').text)



  #return jobs
  