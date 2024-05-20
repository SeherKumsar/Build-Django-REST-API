import requests


headers = {'Authorization': 'Bearer 5ebd20ff26afb614af0fabcf3c3537c3291760ef'}
endpoint = "http://localhost:8000/api/products/" 

data = {
    "title": "This field is done",
    "price": 32.99
}
get_response = requests.post(endpoint, json=data, headers=headers) 
print(get_response.json())