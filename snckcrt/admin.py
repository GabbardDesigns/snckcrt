from django.contrib import admin

class ArticleAdmin(admin.ModelAdmin):

    def render_change_form(self, request, context, *args, **kwargs):
        """We need to update the context to show the button."""
        context.update({'show_save_and_copy': True})
        return super().render_change_form(request, context, *args, **kwargs)
