import requests

# endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

# get_response = requests.get(endpoint, data={"query":
get_response = requests.get(endpoint, json={"query":
    "Hello World"})
# print(get_response) # print source code
print(get_response.text) # raw text response

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
print(get_response.json()) # raw text response
print(get_response.status_code)
