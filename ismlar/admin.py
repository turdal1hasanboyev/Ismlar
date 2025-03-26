from django.contrib import admin

from .models import Category, Name, Likes, Letter


admin.site.register(Category)
admin.site.register(Name)
admin.site.register(Likes)
admin.site.register(Letter)
