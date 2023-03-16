from django.shortcuts import render, redirect
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices, bathroom_choices

from listings.models import Listing, FavouriteItems, Favourite
from realtors.models import Realtor
from .models import Blog, Category, Tag, Tweet, PropertyTag, Subscriber, BlogTag

from django.http import JsonResponse
import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.db.models import Q



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

    if 'area' in request.GET:
        bathrooms = request.GET['bathrooms']
        bedrooms = request.GET['bedrooms']
        area = request.GET['area']
        location = request.GET['location']

        if isinstance(bathrooms, int) and isinstance(bedrooms, int) and isinstance(area, int):
            listings = Listing.objects.filter(
                Q(bathrooms=bathrooms) |
                Q(bedrooms=bedrooms) |
                Q(city__icontains=location) |
                Q(address__icontains=location) |
                Q(county__icontains=location) |
                Q(sqft=area)
            ) # Accessing foreign-keyed values upwards
        else:
             listings = Listing.objects.filter(
                Q(city__icontains=location) |
                Q(address__icontains=location) |
                Q(county__icontains=location) 
            )

            
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






 
 
 
 
 
 # start blog views 
 
 
 
 



#def home(request):
    # Retrieve the latest blog
#    latest_blog = Blog.objects.order_by('-date_posted').first()

    # Retrieve the latest tweet
  #  latest_tweet = Tweet.objects.order_by('-date_posted').first()

  #  context = {
   #     'latest_blog': latest_blog,
    #    'latest_tweet': latest_tweet
   # }

   # return render(request, 'pages/home.html', context)


def blog(request):
    # Retrieve all blogs
    blogs = Blog.objects.all().order_by('-date_posted')

    context = {
        'blogs': blogs
    }

    return render(request, 'pages/blog-classic-sidebar-right.html', context)


def blog_detail(request, blog_id):
    # Retrieve blog with corresponding id
    blog = Blog.objects.get(id=blog_id)

    # Retrieve tags associated with blog
    tags = Tag.objects.filter(blogtag__blog=blog)

    context = {
        'blog': blog,
        'tags': tags
    }

    return render(request, 'pages/blog-classic-sidebar-right.html', context)


def category(request, category_id):
    # Retrieve category with corresponding id
    category = Category.objects.get(id=category_id)

    # Retrieve blogs associated with category
    blogs = Blog.objects.filter(category=category).order_by('-date_posted')

    context = {
        'category': category,
        'blogs': blogs
    }

    return render(request, 'pages/blog-classic-sidebar-right.html', context)


def tag(request, tag_id):
    # Retrieve tag with corresponding id
    tag = Tag.objects.get(id=tag_id)

    # Retrieve blogs associated with tag
    blogs = Blog.objects.filter(blogtag__tag=tag)

    context = {
        'tag': tag,
        'blogs': blogs
    }

    return render(request, 'pages/blog-classic-sidebar-right.html', context)


def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']

        # Create a new subscriber
        subscriber = Subscriber(email=email)
        subscriber.save()

        return render(request, 'pages/blog-classic-sidebar-right.html')

    return render(request, 'pages/blog-classic-sidebar-right.html')


def blog_search(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        # Retrieve blogs that contain the query in either the title or content
        blogs = Blog.objects.filter(title__icontains=query) | Blog.objects.filter(content__icontains=query)

        context = {
            'blogs': blogs,
            'query': query
        }

        return render(request, 'pages/blog-classic-sidebar-right.html', context)


def handler404(request, exception):
    return render(request, 'blog/404.html', status=404)


def handler500(request):
    return render(request, 'blog/500.html', status=500)

 
 
 # End blog views


   
    
    

    
   





