import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/" # "http://127.0.0.1:8000/"
# python py_client/basic.py sadece 8000 portunda çalışıyor.

# get_response = requests.get(endpoint, data={"query":
get_response = requests.get(endpoint, json={"query":
    "Hello World"})
# print(get_response) # print source code
print(get_response.text) # raw text response
print(get_response.status_code)

# requests.get() # Application programming interface

# Phone -> Camera -> App -> API -> CAMERA
# REST APIs -> Web Api
# Http Request
"""
HTTP Request -> HTML
REST API HTTP Request -> JSON (xml)
JavaScript Object Nototion ~ Python Dict
Jason, JSON
"""
print(get_response.json()['message'])
# print(get_response.json()) # raw text response
# print(get_response.status_code)
