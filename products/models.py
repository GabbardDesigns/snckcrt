from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120, blank=False) # max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(blank=False, max_digits=8, decimal_places=2)
    summary = models.TextField(default="Best product ever.")
    active = models.BooleanField(blank=False, default=True)
    alt = models.TextField(blank=True, null=True, default="items")
    imagepath = models.CharField(max_length=120, blank=False, default="https://images.squarespace-cdn.com/content/v1/5a1592ff0abd04e470d48744/1512553461588-BZ9X4L2F5CINL2DU8QTF/ke17ZwdGBToddI8pDm48kPQujXO7frs1W7a77FZyt1F7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0prfa1Z6IeUrCPboCAmmHZn3ZVtqnTHXt-4Tm3byPSNDpHfFtqjKxWw0uc1YBtkl-w/Kaas.jpeg?format=2500w") # max_length = required