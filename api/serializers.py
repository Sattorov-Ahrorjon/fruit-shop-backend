from rest_framework.serializers import ModelSerializer
from .models import User, Product, Order


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'telegram_id', 'first_name', 'last_name', 'username', 'language', 'phone', 'location',
            'latitude', 'longitude'
        )


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'image')


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'name', 'price', 'total_price', 'count')
