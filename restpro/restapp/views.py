from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404, redirect
from .models import Menu,  CartItem
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def kazhicho(request):
    return render(request, 'kazhicho.html')

def reserve(request):
    return render(request,'reservation.html')


def upload_image(request):
    dict1={
        'dict1':Gallery.objects.all()
    }
    return render(request,'gallery.html',dict1)

def about(request):
    return render(request, 'aboutus.html')
def contact(request):
    return render(request, 'contact.html')

from django.views.generic import ListView
class Menulistviews(ListView):
    model = Menu
    template_name ='menu.html'
    context_object_name='dict1'
    


def add_to_cart(request, product_id):
    product = get_object_or_404(Menu, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)  # Associate with user
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    messages.success(request, f'Added {product.name} to cart.')
    return redirect('menu')

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        messages.info(request, 'Your cart is empty.')
    return render(request, 'cart.html', {'cart_items': cart_items})



def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('view_cart')

def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    new_quantity = request.POST.get('quantity')
    if new_quantity.isdigit() and int(new_quantity) > 0:
        cart_item.quantity = int(new_quantity)
        cart_item.save()
        messages.success(request, 'Cart updated successfully.')
    else:
        messages.error(request, 'Invalid quantity. Please enter a positive number.')
    return redirect('view_cart')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to the login page
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})



def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            guests = form.cleaned_data['guests']

            # Send confirmation email
            subject = 'Table Reservation Confirmation'
            message = f'Hello {name},\n\nYour table has been reserved for {guests} guests on {date} at {time}.\n\nThank you!'
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

            return redirect('reservation_success')  # Redirect to a success page
    else:
        form = ReservationForm()

    return render(request, 'reservation.html', {'form': form})

def reservation_success(request):
    return render(request, 'reservation_success.html')


def checkout(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']

            subject = 'Order Confirmation'
            message = f'Thank you for your order, {name}!\n\nYour order will be shipped to:\n{address}'
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
        messages.success(request, "Your order has been placed successfully!")
        return redirect('order_success')  

    cart_items = CartItem.objects.filter(user=request.user)  
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })

def order_success(request):
    CartItem.objects.filter(user=request.user).delete()
    
    return render(request,'order_success.html')


def place_order(request):
    if request.method == 'POST':
        order_success = True  

        if order_success:
          
            CartItem.objects.filter(user=request.user).delete()  

            messages.success(request, 'Your order has been placed successfully!')
            return redirect('order_success') 
    return render(request, 'checkout.html')