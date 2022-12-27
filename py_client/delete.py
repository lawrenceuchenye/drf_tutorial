
import requests

endpoint="http://localhost:8000/api/products/"
get_res=requests.delete(endpoint)
print(get_res.json())



