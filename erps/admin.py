from django.contrib import admin
from .models import Product, Inbound, Outbound, Invetory


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Inbound)
admin.site.register(Outbound)
admin.site.register(Invetory)
