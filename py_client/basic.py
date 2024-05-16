import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/"

get_response = requests.get(endpoint) # HTTP Request
# print(get_response) # print source code
print(get_response.text) # raw text response

# requests.get() # Application programming interface

# Phone -> Camera -> App -> API -> CAMERA
# REST APIs -> Web Api
# Http Request




