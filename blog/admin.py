from django.contrib import admin

# Register your models here.
from .models import Post #changed

admin.site.register(Post) #changed
