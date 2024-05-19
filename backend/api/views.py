import json
from django.http import JsonResponse

# Django Models

def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # print(dir(request))
    # request.body
    print(request.GET) # url query params
    print(request.POST)
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # string of JSON data -> Python Dict
    except:
        pass
    # print(data.keys()) # dict_keys(['query']) basic.py dan gelen
    print(data)
    # data['headers'] = request.headers # request.META ->
    # TypeError: Object of type HttpHeaders is not JSON serializable
    # print(request.headers)
    # json.dumps(dict(request.headers))
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)