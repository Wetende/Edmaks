from django.contrib import admin

from .models import Blog, Category, Tag, PropertyTag, Tweet, Subscriber, BlogTag


admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(PropertyTag)
admin.site.register(Tweet)
admin.site.register(Subscriber)
admin.site.register(BlogTag)


# Register your models here.
