from django.contrib import admin
from .models import (
    Customer,
    Restaurants,
    Menu,
    Cart,
    Order,
    OrderItem
)

# =========================
# CUSTOMER
# =========================
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("user", "mobile", "address")


# =========================
# RESTAURANTS
# =========================
@admin.register(Restaurants)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("Res_name", "Food_cat", "rating")


# =========================
# MENU
# =========================
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("item_name", "restaurant", "price", "is_available")
    list_filter = ("restaurant", "category")
    search_fields = ("item_name",)


# =========================
# CART
# =========================
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "item")


# =========================
# ORDER
# =========================
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "total_amount", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("user__username", "user__email")


# =========================
# ORDER ITEM
# =========================
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "menu_item", "price")
