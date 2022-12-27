from django.http import JsonResponse,HttpResponse
import json

from django.forms.models import model_to_dict
from products.models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

# Create your views here.

@api_view([ "POST" ])
def api_home(request,*args,**kwargs):
    #product=Product.objects.order_by("?").first()
    serializer=ProductSerializer(data=request.data)
    
    print(request.data)
    if serializer.is_valid(raise_exception=True):
        instance=serializer.save()
        print(instance)
        return Response(serializer.data)
    return Response({"message":"Bad Data"})

#    if product:
 #       data=ProductSerializer(product).data
        #data=model_to_dict(product,fields=["id","title","price","sale_price"])
