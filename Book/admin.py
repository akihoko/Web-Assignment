from django.contrib import admin

# Register your models here.
from Book.models import items, movies


class itemAdmin(admin.ModelAdmin):
    list_display = ("hotel_name","hotel_img")

class hotelAdmin(admin.ModelAdmin):
    list_display = ("hotel","description","logo","img1","img2","img3","img4")

admin.site.register(items,itemAdmin)
admin.site.register(movies,hotelAdmin)
