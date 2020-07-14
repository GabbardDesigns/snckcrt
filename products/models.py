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



class Cart:

    def __init__(self):
        self.cart = []

    def __len__(self):
        return len(self.cart)

    def addtocart(self, inventory, selection):

        confirm = input(f'Add {inventory[selection]["title"]} to your cart? (y/n)  ')

        if confirm == 'y':
            print(f'{inventory[selection]["title"]} successfully added to cart.')
            self.cart.append(inventory[selection])
        else:
            print('Well, alright then.  Bye.')

    def removefromcart(self, selection):
        confirm = input(f'Remove {self[selection]["title"]} from your cart? (y/n)  ')
        self.cart.remove(selection)
        #
        # if confirm == 'y':
        #     print(f'{inventory[selection]["title"]} successfully added to cart.')
        #     self.cart.append(inventory[selection])
        # else:
        #     print('Well, alright then.  Bye.')


    def calculateTotal(self):
        total = 0.00
        for c, items in enumerate(self.cart, 0):
            total += float(items["price"])
        return total

    def showcart(self):
        for c, items in enumerate(self.cart, 0):
            print(f'{c:<3} |   {items["title"]:<20} |   {items["price"]:>8}')
