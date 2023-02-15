from django.shortcuts import render, redirect
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices, bathroom_choices

from listings.models import Listing, FavouriteItems, Favourite
from realtors.models import Realtor
from .models import Blog, Category, Tag, Tweet, PropertyTag, Subscriber

from django.http import JsonResponse
import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required



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

    
    search = request.GET.get('search') if request.GET.get('search') != None else ''
    
    if(search):
        listings = Listing.objects.filter(
            Q(room_title__name__icontains=search) |
            Q(name__icontains=search) |
            Q(description__icontains=search) 
        
        ) # Accessing foreign-keyed values upwards
        
    else:    
        listings = Listing.objects.order_by('-list_date').filter(is_published=True)

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
    latest_tweets = Tweet.objects.all().order_by('date_posted')[:5]
    categories = Category.objects.all()
    tags = Tag.objects.all()

        
       
    return render(request, 'pages/blog-classic-sidebar-right.html', {'blogs': blogs, 'latest_tweets': latest_tweets, 'categories': categories, 'tags': tags})
    recent_properties = Listing.objects.all().order_by('-list_date')[:5]
    
  
    recent_properties = Listing.objects.all().order_by('-list_date')[:5]
    
    if title:
        title = Listing.objects.get(id=title)
        property_tags = PropertyTag.objects.filter(title=title)
        return render(request, 'pages/blog-classic-sidebar-right.html', {'title': title, 'property_tags': property_tags})
    
    return render(request, 'pages/blog-classic-sidebar-right.html', {'blogs': blogs, 'latest_tweets': latest_tweets, 'categories': categories, 'recent_properties': recent_properties, 'tags': tags})


# def recent_properties(request):
    #recent_properties = Listing.objects.all().order_by('list_date')[:5]
   # return render(request, 'blog/recent_properties.html', {'recent_properties': recent_properties})

def shop(request):
    listings = Listing.objects.all()
    favourites = []

    if request.user.is_authenticated:
        favourite = Favourite.objects.get(user=request.user, complete=False)
        favouriteitems = favourite.favouriteitems.all()

        for fav in favouriteitems:
            favourites.append(fav.listing.id)

    context = {"listings":listings, "favourites":favourites}
    return render(request, 'pages/shop-list.html', context)

@login_required
def shop_detail(request, pk):
    listing = Listing.objects.get(id=pk)
    listings = Listing.objects.all()

    context = {
        "listing":listing,
        "listings":listings,

        }

    return render(request, 'pages/shop-single.html', context)
    

@login_required
def cart(request):
    favourite = None
    favouriteitems = []

    if request.user.is_authenticated:
        favourite, created = Favourite.objects.get_or_create(
            user=request.user, complete=False)
        favouriteitems = favourite.favouriteitems.all()
    
    
    context = {
        "favourite":favourite,
        "favouriteitems":favouriteitems
    }
    print(favourite)
    return render(request, 'pages/shop-cart.html', context)


def add_cart(request):
    data = json.loads(request.body)
    listing_id = data['id']
    listing = Listing.objects.get(id=listing_id)
    total_items = 0

    if request.user.is_authenticated:
        favourite, created = Favourite.objects.get_or_create(
            user=request.user, complete=False)
        favouriteitem, created = FavouriteItems.objects.get_or_create(
            listing=listing, favourite=favourite)
        if created:
            favouriteitem.quantity += 1
            total_items = favourite.total_items
            favouriteitem.save()
            messages.info(request, "Added to Cart")

        else:
            favouriteitem.quantity = 1
            total_items = favourite.total_items
            messages.info(request, "Added to Cart")
    return JsonResponse(total_items, safe=False)


def update_cart(request):
    data = json.loads(request.body)
    listing_id = data['id']
    new = data['new']
    listing = Listing.objects.get(id=listing_id)

    if request.user.is_authenticated:
        favourite, created = favourite.objects.get_or_create(
            user=request.user, complete=False)
        favouriteitem, created = FavouriteItems.objects.get_or_create(
            listing=listing, favourite=favourite)
        favouriteitem.quantity = new
        favouriteitem.save()
    return JsonResponse('OK', safe=False)


def remove_cart(request):
    data = json.loads(request.body)
    listing_id = data['id']
    listing = Listing.objects.get(id=listing_id)

    if request.user.is_authenticated:
        favourite = Favourite.objects.get(user=request.user, complete=False)
        favouriteitem = FavouriteItems.objects.get(
            listing=listing, favourite=favourite)
        favouriteitem.delete()
    return JsonResponse('OK', safe=False)


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





def subscribe(request):
  if request.method=="POST":
     post = Subscriber() 
    
     email = request.POST['email']
     post.email = email
     post.save()
     return render(request, 'footer.html')
  else:
     return HttpResponseBadRequest('Bad request')


   
    
    

    
   





