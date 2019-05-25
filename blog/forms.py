from django import forms

from . import models

class CreateBlog(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body']
