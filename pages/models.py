from django.db import models
from listings.models import Listing

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blogs/images', blank=True, null=True)


#Category model represents the different categories of properties, such as apartments and houses
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

    
#The Tag model represents the tags that can be associated with properties, such as business and real estate.
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
#The PropertyTag model is used to associate properties with tags.
class PropertyTag(models.Model):
    title = models.ForeignKey(Listing, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    


# the Tweet model represents the latest tweet that will be displayed on the site.
class Tweet(models.Model):
    content = models.CharField(max_length=280)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Subscriber(models.Model):
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.email