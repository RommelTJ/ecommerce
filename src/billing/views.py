from django.shortcuts import render
from django.conf import settings

import stripe
stripe.api_key = settings.STRIPE_API_KEY
STRIPE_PUB_KEY = settings.STRIPE_PUB_KEY


# Create your views here.
def payment_method_view(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY})
