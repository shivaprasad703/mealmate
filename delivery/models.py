from django.db import models
from django.contrib.auth.models import User


# =========================
# CUSTOMER (extends Django User)
# =========================
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username


# =========================
# RESTAURANTS
# =========================
class Restaurants(models.Model):
    Res_name = models.CharField(max_length=100)
    Food_cat = models.CharField(max_length=200)
    rating = models.FloatField()
    img = models.URLField(
        default="https://www.foodiesfeed.com/wp-content/uploads/2023/06/burger-with-melted-cheese.jpg"
    )
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.Res_name


# =========================
# MENU ITEMS
# =========================
from django.db import models

class Menu(models.Model):
    restaurant = models.ForeignKey(
        Restaurants, on_delete=models.CASCADE, related_name="menus"
    )
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=100)

    # 🔥 IMAGE FIELD
    image = models.ImageField(upload_to="menu_items/", blank=True, null=True)

    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.item_name} ({self.restaurant.Res_name})"



# =========================
# CART
# =========================
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.item.item_name}"



  # =========================
# ORDER
# =========================
class Order(models.Model):
    STATUS_CHOICES = (
        ("Paid", "Paid"),
        ("Preparing", "Preparing"),
        ("Out for Delivery", "Out for Delivery"),
        ("Delivered", "Delivered"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.FloatField()
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="Paid"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"


# =========================
# ORDER ITEMS
# =========================
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return f"{self.menu_item.item_name} (Order #{self.order.id})"

