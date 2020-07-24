from django.db import models
from django.utils.html import mark_safe


class Product(models.Model):
    title = models.CharField("Product Name", max_length=120, blank=False)
    price = models.DecimalField("Price per Unit", blank=False, max_digits=8, decimal_places=2)
    imagepath = models.ImageField("Image", upload_to='documents/images', default="", null=True)
    alt = models.TextField("Alt Image Text", blank=True, null=True, default="items")
    active = models.BooleanField("Show this product in my inventory.", blank=False, default=True)

    def __str__(self):
        return '{}'.format(self.title)

    def url(self):
        return '/media/{}'.format(self.imagepath)

    @property
    def thumbnail_preview(self):
        if self.imagepath:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.imagepath.url))
        return ""


