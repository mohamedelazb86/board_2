from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        # fields='__all__'
        exclude=('post','publish_date')