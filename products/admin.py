import json
from django.contrib import admin
from adminplus.sites import AdminSitePlus
from django.utils.safestring import mark_safe
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from copy import deepcopy

from django.contrib.admin import AdminSite
from .models import Product
from .views import product_upload
#
# class MyAdminSite(AdminSite):
#     site_header = 'Monty Python administration'
#
#     def get_urls(self):
#         from django.conf.urls import url
#         urls = super(MyAdminSite, self).get_urls()
#         # Note that custom urls get pushed to the list (not appended)
#         # This doesn't work with urls += ...
#         urls = [
#                    url(r'^product_upload/$', self.admin_view(product_upload))
#                ] + urls
#         return urls
#
#
# admin_site = MyAdminSite(name='myadmin')
# admin_site.register(Product)

# Register your models here.
class UserAdmin(UserAdmin):

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(UserAdmin, self).get_fieldsets(request, obj)
        if not obj:
            return fieldsets

        if not request.user.is_superuser or request.user.pk == obj.pk:
            fieldsets = deepcopy(fieldsets)
            for fieldset in fieldsets:
                if 'is_superuser' in fieldset[1]['fields']:
                    if type(fieldset[1]['fields']) == tuple:
                        fieldset[1]['fields'] = list(fieldset[1]['fields'])
                    fieldset[1]['fields'].remove('is_superuser')
                    break

        return fieldsets


User = get_user_model()
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):

    list_display = ['title', 'price','active']
    ordering = ('title',)
    actions = ['upload_csv']
    template = ['admin/base_site.html']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        inventory = Product.objects.exclude(active=False).values()
        with open('snckcrt/static/data/refund.json', 'w') as teacherfile:
            teacherfile.write('[')
            for count, product in enumerate(inventory):
                json.dump(product, teacherfile, cls=DjangoJSONEncoder)
                if count < len(inventory)-1:
                    teacherfile.write(', ')
            teacherfile.write(']')
            teacherfile.close()


class ImageAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    fields = ('title','imagepath','price','image_tag')
    readonly_fields = ('image_tag',)

    def product_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image_tag.url,
            width=obj.image_tag.width,
            height=obj.image_tag.height,
        )
        )
