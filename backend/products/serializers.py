from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title

class OtherProducts(serializers.Serializer):
    url=serializers.HyperlinkedIdentityField(view_name="product-detail",lookup_field="pk",read_only=True)
    title=serializers.CharField(read_only=True)

class UserPublicData(serializers.Serializer):
    username=serializers.CharField(read_only=True)
    id=serializers.IntegerField(read_only=True)
    is_staff=serializers.BooleanField(read_only=True)
    other_products=serializers.SerializerMethodField(read_only=True)

    def get_other_products(self,obj):
        user_products=obj.user_product.all()[5:]
        return OtherProducts(user_products,many=True,context=self.context).data

class  ProductSerializer(serializers.ModelSerializer):
    update_url=serializers.SerializerMethodField(read_only=True)
    url=serializers.HyperlinkedIdentityField(
        view_name="product-update",
        lookup_field="pk"
    )
    title=serializers.CharField(validators=[validate_title])
    user=UserPublicData(read_only=True)


    class Meta:
        model=Product
        fields=[
            "user",
            "url",
            "update_url",
            "pk",
            "title",
            "desc",
            "price"
            ]

    def create(self,validated_data):
        print(validated_data)
        validated_data.pop("email")
        obj=super().create(validated_data)
        return obj

    def get_update_url(self,obj):
        request=self.context.get("request")
        if request is None:
            return None
        return reverse("product-update",kwargs={"pk":obj.pk},request=request)

