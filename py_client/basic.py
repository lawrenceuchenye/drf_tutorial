
import requests
from getpass import getpass

endpoint_authtoken="http://localhost:8000/api/authtoken/"
endpoint="http://localhost:8000/api/products/"

password=getpass()

authtoken_res=requests.post(endpoint_authtoken,json={"username":"law","password":password})

if authtoken_res.status_code == 200:
    token=authtoken_res.json()["token"]
    headers={
        "Authorization":f"Bearer {token}"
    }
    product_res=requests.get(endpoint,headers=headers)
    print(product_res.json())
print(authtoken_res.json())





