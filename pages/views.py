from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices, state_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices
    }
    # return HttpResponse('<h1> Hello Django </h1>')
    return render(request, 'pages_templates/index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    seller_of_the_month = Realtor.objects.all().filter(seller_of_the_month=True)

    context = {
        'realtors' : realtors, 
        'seller_of_the_month' : seller_of_the_month
    }
    
    return render(request, 'pages_templates/about.html', context)
    
