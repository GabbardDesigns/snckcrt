from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField("Product Name", max_length=120, blank=False)
    #description = models.TextField(blank=True, null=True)
    price = models.DecimalField("Price per Unit", blank=False, max_digits=8, decimal_places=2)
    #summary = models.TextField(default="Best product ever.")
    imagepath = models.ImageField("Image", upload_to='documents/images', default="", null=True)
    alt = models.TextField("Short Description", blank=True, null=True, default="items")
    active = models.BooleanField("Show this product in my inventory.", blank=False, default=True)

