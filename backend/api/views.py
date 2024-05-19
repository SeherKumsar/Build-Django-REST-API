import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):

    # request -> HttpRequest -> Django
    # print(dir(request))
    # request.body
    body = request.body # byte string of JSON data
    print(body)
    return JsonResponse(
        {
            "message":"Hi there, this is your Django API response!!"
        }
    )
