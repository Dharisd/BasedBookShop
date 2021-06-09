from django import template
from shop.models import Product,ImageAlbum

register = template.Library()

@register.simple_tag
def get_default_image(product):
    return product.album.default().image.url