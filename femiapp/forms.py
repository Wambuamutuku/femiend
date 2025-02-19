from django import  forms
from femiapp.models import Post


class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control form-control-lg',
                'accept': 'image/*',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter your full name',

            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter your location',

            }),
            'story': forms.Textarea(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Share your story with us here...',
                'rows': 6,

            }),
        }
