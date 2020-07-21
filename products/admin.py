import json
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from copy import deepcopy

# Register your models here.
from .models import Product
from django.db.models.fields.files import ImageFieldFile


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
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        inventory = list(Product.objects.exclude(active=False).values())
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
