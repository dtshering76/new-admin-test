from django.contrib import admin
from .models import Movie, Customer
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    fields = ['year','title','length']
    search_fields = ['title','length']
    list_display =['title','year','length']
    list_filter = ['year','length']
    list_editable = ['length']
    
    
admin.site.register(Movie,MovieAdmin)
admin.site.register(Customer)