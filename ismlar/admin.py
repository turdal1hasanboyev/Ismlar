from django.contrib import admin

from .models import Category, Name, Likes, Letter


admin.site.site_header = "Ismlar Admin Panel"
admin.site.site_title = "ismlar Admin Panel"
admin.site.index_title = "Welcome to Ismlar Admin Panel!"

admin.site.register(Category)
admin.site.register(Name)
admin.site.register(Likes)
admin.site.register(Letter)
