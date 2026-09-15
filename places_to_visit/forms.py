from django import forms

class PlaceForm(forms.Form):
    name = forms.CharField()
    place_type = forms.CharField()
    location = forms.CharField(required=False)
    rating = forms.IntegerField(min_value=1, max_value=5)
    description = forms.CharField(widget=forms.Textarea)