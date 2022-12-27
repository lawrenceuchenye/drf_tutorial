
import requests

endpoint_200="https://httpbin.org/status/200"
endpoint="http://localhost:8000/api/products/8/"

get_res=requests.get(endpoint)
print(get_res.json())




