from django.contrib import admin
from .models import Image,ImageAlbum,Category,Product
# Register your models here.



#set council branding
admin.site.site_title = "Bookshop Admin"
admin.site.site_header = "Bookshop Dashboard"
admin.site.index_title = "Dashboard"


# Register your models here.
admin.site.register(Image)
admin.site.register(ImageAlbum)
admin.site.register(Category)




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","featured")



