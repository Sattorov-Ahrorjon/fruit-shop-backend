from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User, Product, Order
from django.conf import settings


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'telegram_id', 'first_name', 'last_name', 'username', 'language', 'phone', 'location',
            'latitude', 'longitude'
        )


class ProductSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        lang = 'uz'
        if request and request.META.get('HTTP_ACCEPT_LANGUAGE') in settings.MODELTRANSLATION_LANGUAGES:
            lang = request.META.get('HTTP_ACCEPT_LANGUAGE')
        self.fields['name'] = serializers.CharField(source=f"name_{lang}")
        self.fields['description'] = serializers.CharField(source=f"description_{lang}")

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'amount', 'image')


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'name', 'price', 'total_price', 'count')
