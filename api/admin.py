from django.contrib import admin
from .models import User, Product, Order


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username')
    list_display_links = ('id', 'first_name', 'last_name', 'username')
    search_fields = ('first_name', 'last_name', 'username')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_active')
    list_display_links = ('id', 'name')
    list_filter = ('is_active',)
    search_fields = ('name', 'price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'price', 'count', 'total_price')
    list_display_links = ('id', 'name', 'user')
    list_filter = ('user', 'price')
    search_fields = ('name', 'user__first_name', 'user__last_name')
