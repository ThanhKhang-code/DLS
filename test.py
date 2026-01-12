import requests

url = "https://raw.githubusercontent.com/ThanhKhang-code/DLS/main/Whitelist.txt"
r = requests.get(url)
print(r.status_code)
print(r.text)
