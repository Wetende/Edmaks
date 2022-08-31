from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices, property_type, bathroom_choices

from .models import Listing

def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 3)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }

  return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)

  context = {
    'listing': listing
  }

  return render(request, 'listings/listing.html', context)

def search(request):
  queryset_list = Listing.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)

  # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
    'state_choices': state_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'listings': queryset_list,
    'values': request.GET
  }

  return render(request, 'listings/search.html', context)

def submit(request):
  if request.method == 'POST'and request.FILES['photo']:
    # Get form values
    title = request.POST['title']
    p_type = request.POST['p_type']
    city = request.POST['city']
    price = request.POST['price']
    address = request.POST['address']
    area = request.POST['area']
    bedrooms = request.POST['bedroom']
    bathrooms = request.POST['bathroom']
    county = request.POST['state']
    postal_code = request.POST['postal_code']
    description = request.POST['description']
    photo_main = request.FILES['photo']

    property = Listing.objects.create(title=title, p_type=p_type, city=city, price=price, 
                                    address=address, sqft=area, bedrooms=bedrooms,
                                    bathrooms=bathrooms, county=county, postal_code=postal_code, description=description, photo_main=photo_main)
    property.save()
    return redirect('index')
  
  context = {
    'state_choices': state_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'property_type':property_type,
    'bathroom_choices':bathroom_choices
   
  }

  return render(request, 'listings/submit-property.html', context)