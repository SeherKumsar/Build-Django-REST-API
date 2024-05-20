from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"]) 
# @api_view dekoratörü, gelen isteği bir Django HttpRequest nesnesinden bir DRF Request nesnesine dönüştürür.
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    # data = request.POST
    # return JsonResponse(data)

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # instance = serializer.save(commit=False)
        # instance = form.save()
        # print(serializer.data)
        # print(instance)
        print(serializer.data)
        data = serializer.data
        return Response(data)
    return Response({"invalid": "not good data"}, status=400)