from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from . import validators
# from .validators import validate_title
from . import validators

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
            view_name='product-detail',
            lookup_field='pk'
    )
    # title = serializers.CharField(validators=[validate_title])
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    # name = serializers.CharField(source="title", read_only=True)
    # email = serializers.EmailField(ource="user.email", read_only=True)
    # email = serializers.EmailField(write_only=True)
    # email = serializers.EmailField()
    class Meta:
        model = Product
        fields = [
            # 'user',
            'url',
            'edit_url',
            'pk',
            'title',
            # 'email',
            # 'name',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    # def validate_title(self, value): # validate_<fieldname>
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     # qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value

    # def create(self, validated_data):
    #     # return Product.obejcts.create(**validated_data)
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     # instance.title = validated_data.get('title')
    #     # return instance
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)

    def get_url(self, obj):
        # return f"/api/v2/products/{obj.pk}/"
        request = self.context.get('request') # self.request
        if request is None:
            return None
        return reverse("", kwargs={"pk": obj.pk}, request=request)

    def get_edit_url(self, obj):
        request = self.context.get('request') # self.request
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
    
    def get_my_discount(self, obj):
        # try:
        #     return obj.get_discount()
        # except:
        #     return None
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()