from django.contrib import admin
from .models import Contact, User, Post, Admin

# Register your models here.
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Admin)
