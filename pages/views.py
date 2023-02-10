from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices, bathroom_choices

from listings.models import Listing
from realtors.models import Realtor
from .models import Blog, Category, Tag, Tweet, PropertyTag

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
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings
    }
    return render(request, 'pages/properties-list-rightside.html', context)




def list(request):
    return render(request, 'pages/properties-list-rightside.html')

def grid(request):
    return render(request, 'pages/properties-grid-rightside.html')


def agents(request):
    return render(request, 'pages/agent-grid-3.html')

def blog(request):
    blogs = Blog.objects.all()
    latest_tweets = Tweet.objects.all().order_by('-date_posted')[:5]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    recent_properties = Listing.objects.all().order_by('-date_posted')[:5]
    
    if title:
        title = Listing.objects.get(id=title)
        property_tags = PropertyTag.objects.filter(title=title)
        return render(request, 'pages/blog-classic-sidebar-right.html', {'title': title, 'property_tags': property_tags})
    
    return render(request, 'pages/blog-classic-sidebar-right.html', {'blogs': blogs, 'latest_tweets': latest_tweets, 'categories': categories, 'recent_properties': recent_properties, 'tags': tags})


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




