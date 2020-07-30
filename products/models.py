from django.db import models
from django.utils.html import mark_safe


class Product(models.Model):
    title = models.CharField("Product Name", max_length=120, blank=False)
    price = models.DecimalField("Price per Unit", blank=False, max_digits=8, decimal_places=2)
    imagepath = models.ImageField("Image", upload_to='documents/images', default="", null=True)
    alt = models.CharField("Alt Image Text", max_length=120, blank=True, null=True, default="items")
    active = models.BooleanField("Show this product in my inventory.", blank=False, default=True)

    def __str__(self):
        return '{}'.format(self.title)

    def url(self):
        return '/media/{}'.format(self.imagepath)

    @property
    def thumbnail_preview(self):
        """    This function is called on self and assigns a thumbnail preview that
               is used in the amdin/edit_product_view.  It defines a “safe” snippet
               of html code that is returned by the function, effectively allowing
               relational images of any product page.
        """
        if self.imagepath:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.imagepath.url))
        return ""


