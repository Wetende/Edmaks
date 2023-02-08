from email.policy import default
from secrets import choice
from django.db import models
from datetime import datetime
from realtors.models import Realtor
from django.contrib.auth.models import User


property_type = [
  ('Apartment',  'Apartment'),
  ('Office', 'Office'),
  ('House', 'House'),
  ('Villa', 'Villa'),
  ('Commercial', 'Commercial'),
  ('Others', 'Others')
]




class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, blank=True, null=True)
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  county = models.CharField(max_length=100)
  postal_code = models.CharField(max_length=20)
  description = models.TextField(blank=True)
  p_type = models.CharField(max_length=100, choices=property_type, default='Office', blank=True, null=True)
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
  garage = models.IntegerField(default=0)
  sqft = models.IntegerField()
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)


  def __str__(self):
    return self.title