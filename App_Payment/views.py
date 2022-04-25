from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# MODELS AND FORMS
from App_Order.models import Order
from App_Payment.forms import BillingAddress
from App_Payment.forms import BillingForm

# FOR PAYMENT 
import requests
from sslcommerz_lib import SSLCOMMERZ
#from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import socket

# Create your views here.

@login_required
def checkout(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    form = BillingForm(instance=saved_address)
    if request.method == 'POST':
        form = BillingForm(request.POST, instance=saved_address)
        if form.is_valid():
            form.save()
            form = BillingForm(instance=saved_address)
            messages.success(request, f'Shipping Address Save!')
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_items = order_qs[0].orderitems.all()
    order_total = order_qs[0].get_totals()
    return render(request, 'App_Payment/checkout.html', context={'form':form, 'order_items':order_items, 'order_total':order_total, 'saved_address':saved_address})

@login_required
def payment(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    if not saved_address[0].is_fully_filled():
        messages.info(request, f'Please complate shipping address!')
        return redirect('App_Payment:checkout')

    if not request.user.profile.is_fully_filled():
        messages.info(request, f'Please complete profile details!')
        return redirect('App_Login:profile')

   # mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id='your_sslc_store_id', sslc_store_pass='your_sslc_store_passcode')
    
   # sslcz = SSLCOMMERZ({ 'store_id': <your_store_id>, 'store_pass': <your_password>, 'issandbox': True })


    return render(request, 'App_Payment/payment.html', context={})