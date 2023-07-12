from django.contrib import admin
from . models import Coffee

@admin.register(Coffee) #admini kişileştireceğiz
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', "price") #listeliyor
    list_filter = ('price',) #virgül ekle ki text olarak gördüğünden hata almayasın
    search_fields = ('name', 'description') #arama seçeneği ekliyor
    