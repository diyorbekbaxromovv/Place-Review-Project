from django.contrib import admin
from .models import Place, Owner, PlaceOwner, PlaceComment, Category, Meal
# Register your models here.

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'address')
    search_fields = ('id', 'name')
    
    
admin.site.register(Place, PlaceAdmin)

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'bio')
    search_fields = ('id', 'first_name')
    
admin.site.register(Owner, OwnerAdmin)
    
admin.site.register(PlaceOwner)
admin.site.register(PlaceComment)
admin.site.register(Category)
admin.site.register(Meal)