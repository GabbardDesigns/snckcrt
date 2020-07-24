from django import forms
from .models import Product


class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'price',
            'active',
            'imagepath',
            'alt',
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not ':' in title[:4]:
            raise forms.ValidationError("This is not a valid title.")
        return title


class RawProductForm(forms.Form):
    title = forms.CharField(label='')
    description = forms.CharField(required=True, widget=forms.Textarea)
    price = forms.DecimalField(initial='199.99')
    summary = forms.CharField()
    docfile = forms.FileField(
        label='Select a file',
    )





