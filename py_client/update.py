
import requests

endpoint_200="https://httpbin.org/status/200"
endpoint="http://localhost:8000/api/products/update/3/"

data={
    "title":"Pig Meat",
    "price":15.12
}

get_res=requests.get(endpoint,json=data)
#print(get_res.text)
#print(get_res.headers)
print(get_res.json())





