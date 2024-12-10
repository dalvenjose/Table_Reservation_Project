from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', kazhicho, name='home'),
    path('upload/', upload_image, name='upload_image'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('menu/', Menulistviews.as_view(), name='menu'),
    path('cart/', view_cart, name='view_cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('update_cart/<int:item_id>/', update_cart, name='update_cart'),
    path('', register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('reserve/', reserve_table, name='reserve_table'),
    path('reservation-success/', reservation_success, name='reservation_success'),
    path('reserve/',reserve,name="reserve"),
    path('checkout/',checkout, name='checkout'),
    path('order-success/', order_success, name='order_success'),
    path('place-order/', place_order, name='place_order'),
]
