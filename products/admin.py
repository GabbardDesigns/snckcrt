from django.contrib import admin

# Register your models here.

from .models import Product

admin.site.register(Product)

# modify Admin page

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from copy import deepcopy


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