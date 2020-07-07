from django import forms

from .models import Product


class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary',
            'active'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not ':' in title[:4]:
            raise forms.ValidationError("This is not a valid ittle.")
        return title


class RawProductForm(forms.Form):
    title = forms.CharField(label='')  # max_length = required
    description = forms.CharField(required=True, widget=forms.Textarea)
    price = forms.DecimalField(initial='199.99')
    summary = forms.CharField()
