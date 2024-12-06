from django import  forms
from femiapp.models import Post


class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your location',
            }),
            'story': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Share your story...',
                'rows': 5,
            }),
        }