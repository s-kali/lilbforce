import requests

payload = {'username':'admin', 'password':'', 'Login': 'Login', 'user_token':''}

r = requests.get('http://172.17.0.2/vulnerabilities/brute/', params=payload)

print(r.text)
