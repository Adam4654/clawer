from wsgiref import headers
from wsgiref.headers import Headers

import requests

headers={
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

parametre={

}

url = "https://github.com/"
resp = requests.get(url)

print(resp.status_code)
print(resp.text)