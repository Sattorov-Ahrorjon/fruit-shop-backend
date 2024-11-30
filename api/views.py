from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ViewSet
from .serializers import UserSerializer, ProductSerializer, OrderSerializer
from .models import User, Product, Order
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=UserSerializer(),
        responses={201: UserSerializer()},
        tags=['User'],
    )
    def user_create(self, request):
        data = request.data
        tg_id = data.get('telegram_id')
        user = User.objects.filter(telegram_id=tg_id).first()
        serializer = UserSerializer(data=request.data, context={'request': request})
        lang = False
        if user:
            lang = user.language if True else False
            serializer = UserSerializer(user, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data={'result': serializer.data, 'ok': True, 'lang': lang}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: UserSerializer()},
        tags=['User'],
    )
    def user_list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: UserSerializer()},
        tags=['User'],
    )
    def user_detail(self, request, pk):
        user = User.objects.filter(id=pk).first()
        if not user:
            return Response(data={'result': '', 'ok': False}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: UserSerializer()},
        tags=['User'],
    )
    def user_check(self, request, pk):
        user = User.objects.filter(telegram_id=pk).first()
        if user is None or user.language in None:
            return Response(data={'result': '', 'ok': False, 'lang': False}, status=status.HTTP_404_NOT_FOUND)
        return Response(data={'result': '', 'ok': True}, status=status.HTTP_200_OK)


class ProductViewSet(ViewSet):
    @swagger_auto_schema(
        responses={200: ProductSerializer()},
        tags=['Product'],
    )
    def product_detail(self, request, pk):
        product = Product.objects.filter(id=pk).first()
        if not product:
            return Response(data={'result': '', 'ok': False}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: ProductSerializer()},
        tags=['Product'],
    )
    def product_list(self, request):
        products = Product.objects.filter(is_active=True)
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)


class OrderViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=OrderSerializer(),
        responses={201: OrderSerializer()},
        tags=['Order'],
    )
    def order_create(self, request):
        serializer = OrderSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={200: OrderSerializer()},
        tags=['Order'],
    )
    def order_list(self, request, pk):
        orders = Order.objects.filter(user_id=pk)
        serializer = OrderSerializer(orders, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(name='order_name', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ],
        responses={200: OrderSerializer()},
        tags=['Order'],
    )
    def order_detail(self, request, pk):
        order_name = request.query_params.get('order_name')
        order = Order.objects.filter(user_id=pk, name__icontains=order_name).first()
        if not order:
            return Response(data={'result': '', 'ok': False}, status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)
