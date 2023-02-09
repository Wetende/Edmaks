from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts/images', blank=True, null=True)
