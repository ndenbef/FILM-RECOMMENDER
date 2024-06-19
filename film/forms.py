from django import forms

class CollectionCreationForm(forms.Form):
    name = forms.CharField(label='Search', max_length=100)
    
class RatingForm(forms.Form):
    stars = forms.IntegerField(label='Nombre d\'étoiles', min_value=1, max_value=5, widget=forms.TextInput(attrs={'type': 'range', 'class': 'form-range', 'min': 1, 'max': 5}))