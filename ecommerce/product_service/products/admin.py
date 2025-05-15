from django.contrib import admin
from .models import Product, Order, ProductOrder, Payment, Shipping

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'is_active', 'created_at', 'updated_at')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description')
    ordering = ('id',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_number', 'status', 'total_amount', 'created_at')
    list_filter = ('status',)
    search_fields = ('order_number', 'shipping_address')
    ordering = ('-created_at',)

@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
    list_filter = ('order', 'product')
    search_fields = ('order__order_number', 'product__name')
    ordering = ('id',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_id', 'order', 'payment_method', 'paid_at', 'payment_status')
    search_fields = ('customer_id', 'order__id', 'payment_status')
    list_filter = ('payment_status',)

@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'shipping_method', 'shipped_at', 'shipping_status')
    search_fields = ('order__id', 'shipping_status')
    list_filter = ('shipping_status',)
