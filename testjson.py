import requests
from bs4 import BeautifulSoup

site = 'https://haveibeenpwned.com/'

session = requests.Session()
cookies = { 'ai_user' : 'AGj6l|2020-07-12T09:45:59.867Z' }

session.headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.61 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Referer': site
}

resp = session.get(site)
html = resp.text

soup = BeautifulSoup(html , 'lxml')

data = {}
form = soup.find('form')
for field in form.find_all('input'):
	try:
	    data[field['name']] = field['value']
 
	except:
	    pass


data[u'Account'] = "agkl2000@yahoo.fr"

r = requests.post('https://haveibeenpwned.com/', cookies = cookies)

post_resp = session.post('https://haveibeenpwned.com/', data = data)

post_soup = BeautifulSoup(post_resp.content , 'lxml')

test = post_soup.text
result = test.find('Please en')

if (result > 0) :
	print("bon email")
else :
	print("mauvais email")
print(result)

print post_soup.text


