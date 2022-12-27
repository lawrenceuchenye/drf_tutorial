
from django.urls import path
from . import views 

urlpatterns=[
    path("<int:pk>/",views.ProductMixinAPIView.as_view(),name="product-detail"),
    path("create/",views.ProductMixinAPIView.as_view(),name="product-create"),
    path("update/<int:pk>/",views.ProductUpdateAPIView.as_view(),name="product-update"),
    path("delete/<int:pk>/",views.ProductDeleteAPIView.as_view(),name="product-delete"),
    path("",views.ProductMixinAPIView.as_view(),name="product-list")


]
