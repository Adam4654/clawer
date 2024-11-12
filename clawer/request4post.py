import requests

# donnees={
#     ke
# }

url = "https://github.com/"
resp = requests.post(url)

print(resp.status_code)
print(resp.text)