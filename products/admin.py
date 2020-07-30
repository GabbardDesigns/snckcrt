import json
from django.utils.html import format_html
from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .views import write_json
import logging
from copy import deepcopy
from .models import Product
logger = logging.getLogger(__name__)


class UserAdmin(UserAdmin):

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(UserAdmin, self).get_fieldsets(request, obj)

        if not obj:
            return fieldsets

        if not request.user.is_superuser or request.user.pk == obj.pk:
            fieldsets = (
                ('Login', {
                    'fields': ('username',)
                }),
                ('Profile', {
                    'fields': ('first_name', 'last_name', 'email')
                }),
                ('Administrative', {
                    'fields': ('is_staff', 'is_active')
                }),
            )

        return fieldsets

    list_display = ('username', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')


User = get_user_model()
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """   This class super is used to augment the default Admin model for Product.
          It defines the defaults for list display on the admin list_view paes, the default filtering,
          Additional available actions, and the template assigned to product pages.
    """
    list_display = ['title', 'price', 'active']
    ordering = ('title',)
    actions = ['upload_csv']
    template = ['admin/base_site.html']

    def save_model(self, request, obj, form, change):
        """   This function super is used to augment the default Admin save_model behavior for the Product model.
              This function adds a re-write of the inventory JSON file read in by JavaScript on the homepage.
        """
        super().save_model(request, obj, form, change)
        inventory = Product.objects.order_by('title').exclude(active=False).values()
        write_json(inventory)

    def image_tag(self, obj):
        """    This function is called on self and assigns a thumbnail preview that
                      is used in the amdin/edit_product_view.  It defines a “safe” snippet
                      of html code that is returned by the function, effectively allowing
                      relational images of any product page.
               """
        return format_html('<img src="{}" width="100" height="100" alt="Needs image" />'.format(obj.imagepath.url))

    image_tag.short_description = 'Image'

    list_display = ('title', 'price', 'image_tag', )
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True

