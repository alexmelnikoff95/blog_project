from django import forms

from blog.models import Tag, Post


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'slug': 'form-control'})
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'title': 'form-control'}),
            'slug': forms.TextInput(attrs={'slug': 'form-control'}),
            'body': forms.Textarea(attrs={'body': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'tags': 'form-control'})
        }
