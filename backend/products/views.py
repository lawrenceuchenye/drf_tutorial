from rest_framework import generics,mixins,permissions,authentication
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from .models import Product

from .permission import IsStaffEditorPermssion,UserQuerySetMixin
from .authentication import TokenAuthentication
from api.mixins import StaffEditorPermissionMixin

# Create your views here.

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    #lookup_field="pk"

class ListCreateAPIView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

@api_view([ "GET","POST" ])
def product_alt_view(request,pk=None,*args,**kwargs):
    if request.method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # list view
        queryset = Product.objects.all() 
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if method == "POST":
        # create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)
    return Response({"message":"ONLY POST AND GET IS ALLOWED"})

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field="pk"

    permission_classes=[IsStaffEditorPermssion]
    authentication_classes=[
        TokenAuthentication,
        authentication.SessionAuthentication
    ]

    def perform_update(self,serializer):
        model_instance=serializer.save()
        if not model_instance.desc:
            model_instance.desc=model_instance.title

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


    def perform_destroy(self,instance):
        #do dtuff wuth instabce uf needed
        super().perform_destroy(instance)
        

class ProductMixinAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    allow_staff_view_all=True
    permission_classes=[IsStaffEditorPermssion] 
    authentication_classes=[
        authentication.SessionAuthentication,
        TokenAuthentication
    ]
    

    lookup_field="pk"

    def get(self,request,*args,**kwargs):
        pk=kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

