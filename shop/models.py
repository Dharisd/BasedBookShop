from django.db import models

# Create your models here.
class ImageAlbum(models.Model):
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        )
    def default(self):
        return self.images.filter(default=True).first()

    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)

    def __str__(self):
        return (f"{self.name}")

class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE)


    def __str__(self):
        return (f"{self.name}")


class Category(models.Model):
    name = models.CharField(max_length=255)
    album = models.OneToOneField(
        ImageAlbum,
        on_delete=models.CASCADE,
        null=True
    ) 

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return (f"{self.name}")

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE) 
    album = models.OneToOneField(
        ImageAlbum,
        related_name='model',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return (f"{self.name}")



class Carousel(models.Model):
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=512)
    album = models.OneToOneField(
        ImageAlbum,
        on_delete=models.CASCADE,
        null=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

