import requests

endpoint="http://localhost:8000/api/products/create/"
data={
    "title":"Garri",
    "desc":"school cornflakes lol",
    "price":12.00
}

get_res=requests.post(endpoint,json=data)

#print(get_res.text)
#print(get_res.headers)
#print(get_res.json())




