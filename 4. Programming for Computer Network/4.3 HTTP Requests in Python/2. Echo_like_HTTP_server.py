import requests
r = requests.get("https://httpbin.org/get")
print(r.url)
print(r.status_code)
print(r.text)