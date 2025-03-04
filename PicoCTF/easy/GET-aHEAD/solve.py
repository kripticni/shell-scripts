import requests

response = requests.head("http://mercury.picoctf.net:47967/index.php")
print(response.headers)

# the first one that actually required me to write something
