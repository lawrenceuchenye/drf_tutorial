
import requests

endpoint_200="https://httpbin.org/status/200"
endpoint="http://localhost:8000/api/products/create/"

headers={
    "Authorization":"Bearer a2d296e553ef22f07fa0c8bdd8f6311c98e34d3f"
}

get_res=requests.get(endpoint,headers=headers)
print(get_res.json())





