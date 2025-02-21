from django.contrib import admin
from .models import CustomUser
# Register your models here.

# add CustomUser model(table) to admin interface
admin.site.register(CustomUser)