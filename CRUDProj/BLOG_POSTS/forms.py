from django import forms
from .models import PostModel

class PostDetailsForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = '__all__'
