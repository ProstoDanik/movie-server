from django import forms
from main.models import Reviews

class ReviewForm(forms.ModelForm):


    class Meta:
        model = Reviews
        fields = ('film', 'text_reviews', 'rating_number')