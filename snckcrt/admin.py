from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from products.views import get_inventory
from django.contrib import admin
from django.utils.html import format_html

class ArticleAdmin(admin.ModelAdmin):

    def render_change_form(self, request, context, *args, **kwargs):
        """We need to update the context to show the button."""
        context.update({'show_save_and_copy': True})
        return super().render_change_form(request, context, *args, **kwargs)

    def response_post_save_change(self, request, obj):
        """This method is called by `self.changeform_view()` when the form
        was submitted successfully and should return an HttpResponse.
        """
        # Check that you clicked the button `_save_and_copy`
        if '_save_and_copy' in request.POST:
            # Create a copy of your object
            # Assuming you have a method `create_from_existing()` in your manager
            new_obj = self.model.objects.create_from_existing(obj)

            # Get its admin url
            opts = self.model._meta
            info = self.admin_site, opts.app_label, opts.model_name
            route = '{}:{}_{}_change'.format(*info)
            post_url = reverse(route, args=(new_obj.pk,))

            # Update the json file
            get_inventory(request)

            # And redirect
            return HttpResponseRedirect(post_url)
        else:
            # Otherwise, use default behavior
            return super().response_post_save_change(request, obj)

