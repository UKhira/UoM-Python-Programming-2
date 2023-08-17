import requests
r = requests.get("https://www.google.com/search?q=python+http+request")
print(r.url)
print(r.status_code)
print(r.text)