import requests
from bs4 import BeautifulSoup

url = 'http://172.17.0.2/vulnerabilities/brute/'
#payload = {'username':'admin', 'password':'', 'Login': 'Login', 'user_token':''}

session = requests.Session()
response = session.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

for name in soup.find_all('input'):
	if(name.get('name')=='user_token'):
		user_token = name.get('value')

print(user_token)
