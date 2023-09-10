from django import forms
from .models import ProductComment,Category


class SearchForm(forms.Form):
    # Define your filter fields here
    name = forms.CharField(required=False)
    category = forms.ChoiceField(choices=Category.objects.all(), required=False)
    price_min = forms.DecimalField(min_value=0, required=False)
    price_max = forms.DecimalField(min_value=0, required=False)
    # Add more filter fields as needed

        
        
    
    
class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['comment_text']
