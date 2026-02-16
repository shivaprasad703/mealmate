from django.urls import path
from . import views

app_name = "delivery"

urlpatterns = [

    # =========================
    # HOME & STATIC PAGES
    # =========================
    path("", views.home, name="home"),
    path("restaurants/", views.restaurants, name="restaurants"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

    # =========================
    # AUTHENTICATION (CUSTOMERS)
    # =========================
    path("sign-up/", views.sign_up, name="sign_up"),
    path("handle-signup/", views.handle_signup, name="handle_signup"),

    path("sign-in/", views.sign_in, name="sign_in"),
    path("handle-signin/", views.handle_signin, name="handle_signin"),

    path("logout/", views.logout_view, name="logout"),

    # =========================
    # CUSTOMER PROFILE
    # =========================
    path("profile/<str:username>/", views.profile, name="profile"),

    # =========================
    # CUSTOMER – RESTAURANTS & MENUS
    # =========================
    path("cusmenu/<int:id>/<str:username>/", views.cusmenu, name="cusmenu"),

    # =========================
    # CART & CHECKOUT
    # =========================
    path("add-to-cart/<int:id>/<str:username>/", views.add_to_cart, name="add_to_cart"),
    path("cart/<str:username>/", views.show_cart, name="show_cart"),
    path("checkout/<str:username>/", views.checkout, name="checkout"),

    # ===================== ====
    # CUSTOMER ORDERS
    # =========================
    path("orders/<str:username>/", views.orders, name="orders"),

    # =========================
    # ADMIN – AUTH (CUSTOM UI)
    # =========================
    path("admin-login/", views.admin_login, name="admin_login"),
    path("admin-logout/", views.admin_logout, name="admin_logout"),

    # =========================
    # ADMIN – DASHBOARD
    # =========================
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),

    # =========================
    # ADMIN – RESTAURANTS
    # =========================
    path("admin/restaurants/", views.display_res, name="display_res"),
    path("admin/add-restaurant/", views.add_res, name="add_res"),

    # =========================
    # ADMIN – MENUS / ITEMS
    # =========================
    path("admin/view-menu/<int:id>/", views.view_menu, name="view_menu"),
    path("admin/add-menu/<int:id>/", views.add_menu, name="add_menu"),
    path("admin/delete-menu/<int:id>/", views.delete_menu, name="delete_menu"),

    path(
    "admin-panel/restaurants/",
    views.admin_restaurants,
    name="admin_restaurants"
),
    path(
    "admin-panel/delete-restaurant/<int:id>/",
    views.delete_res,
    name="delete_res"
),

path(
    "admin-panel/add-restaurant/",
    views.add_res,
    name="add_res"
),

# ======================
# ADMIN – ITEMS
# ======================

path(
    "admin-panel/items/<int:res_id>/",
    views.view_menu,
    name="view_menu"
),

path(
    "admin-panel/items/add/<int:res_id>/",
    views.add_menu,
    name="add_menu"
),

path(
    "admin-panel/items/delete/<int:item_id>/",
    views.delete_menu,
    name="delete_menu"
),



path("admin-logout/", views.admin_logout, name="admin_logout"),

path(
    "cusdisplay-res/<int:id>/<str:username>/",
    views.cusdisplay_res,
    name="cusdisplay_res"
),

path(
    "cusdisplay-res/<str:username>/",
    views.cusdisplay_res,
    name="cusdisplay_res"
),

path(
    "admin-panel/items/add/<int:res_id>/",
    views.add_menu,
    name="add_menu"
),
path("remove-from-cart/<int:id>/<str:username>/", views.remove_from_cart, name="remove_from_cart"),



path("verify-otp/", views.verify_otp, name="verify_otp"),


path("login-otp/", views.login_otp, name="login_otp"),

path("payment-success/<str:username>/", views.payment_success, name="payment_success"),

path("my-orders/<str:username>/", views.my_orders, name="my_orders"),


path("admin-panel/orders/", views.admin_orders, name="admin_orders"),



path("payment-success/<str:username>/", views.payment_success, name="payment_success"),

path(
    "admin/order-status/<int:order_id>/",
    views.update_order_status,
    name="update_order_status"
),


]
