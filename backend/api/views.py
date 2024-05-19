from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET"]) 
# @api_view dekoratörü, gelen isteği bir Django HttpRequest nesnesinden bir DRF Request nesnesine dönüştürür.
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    # if request.method != "POST":
    #     return Response({"detail": "GET not allowed"}, status=405)
    # model_data = Product.objects.all().order_by("?").first()
    # data = {}
    # if model_data:
    #     data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
    # return Response(data)

    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
        data = ProductSerializer(instance).data
    return Response(data)