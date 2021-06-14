from django.contrib import admin
from registartion.models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    pass

class UserProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Products)
admin.site.register(UserProducts)
