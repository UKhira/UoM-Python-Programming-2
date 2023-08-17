import requests
r = requests.get("https://httpbin.org/obvious-incorrect")
print(r.url)
print(r.status_code)    #status code = 404(not found)
print(r.text)