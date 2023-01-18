from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices, bathroom_choices

from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'bathroom_choices': bathroom_choices,
        'price_choices': price_choices
    }


    return render(request, 'pages/index-5.html', context)

def properties(request):
    return render(request, 'pages/properties-list-rightside.html')

def list(request):
    return render(request, 'pages/properties-list-rightside.html')

def grid(request):
    return render(request, 'pages/properties-grid-rightside.html')


def agents(request):
    return render(request, 'pages/agent-grid-3.html')

def blog(request):
    return render(request, 'pages/blog-classic-sidebar-right.html')

def shop(request):
    listings = Listing.objects.all()

    context = {"listings":listings}
    return render(request, 'pages/shop-list.html', context)

def shop_detail(request, pk):
    listing = Listing.objects.get(id=pk)
    listings = Listing.objects.all()

    context = {
        "listing":listing,
        "listings":listings,

        }

    return render(request, 'pages/shop-single.html', context)
    

def cart(request):
    return render(request, 'pages/shop-cart.html')

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)


