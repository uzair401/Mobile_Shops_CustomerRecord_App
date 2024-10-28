from django.shortcuts import render
from .models import Customer
from django.db.models import Sum
from django.utils import timezone

def dashboard(request):
    total_customers = Customer.objects.count()
    total_mobiles = Customer.objects.count()
    recent_customers = Customer.objects.order_by('-purchase_date')[:5]
    
    if request.method == "POST":
        selected_date = request.POST.get('date')
        purchased_mobiles = Customer.objects.filter(purchase_date=selected_date)
    else:
        purchased_mobiles = None

    return render(request, 'dashboard.html', {
        'total_customers': total_customers,
        'total_mobiles': total_mobiles,
        'recent_customers': recent_customers,
        'purchased_mobiles': purchased_mobiles
    })
