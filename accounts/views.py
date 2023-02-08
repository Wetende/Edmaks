from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from listings.models import Listing
from django.contrib.auth.decorators import login_required

def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')

  else:
    return render(request, 'accounts/register.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  if request.method == 'GET':
    auth.logout(request)
    messages.success(request, 'You are now logged out')
  return redirect('index')

@login_required(login_url='login')
def dashboard(request):
  user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
  listings = Listing.objects.all()

  context = {
    'contacts': user_contacts,
    'listings':listings
  }

  return render(request, 'pages/index-5.html', context)


@login_required(login_url='login')
def favourite_properties(request, user_id):
  return render(request, 'accounts/favorited-properties.html')
  

def my_properties(request, user_id):
  user = User.objects.get(pk=user_id)
  listings = Listing.objects.order_by('-list_date').filter(user=user)

  context = {
        'listings': listings
    }
  
  return render(request, 'accounts/my-properties.html', context)
  
 
def profile(request):
  return render(request, 'accounts/user-profile.html')

def change_password(request):
  return render(request, 'accounts/change-password.html')


def delete(request):
  return render(request, 'accounts/')

def edit(request):
  return render(request, 'accounts/')




