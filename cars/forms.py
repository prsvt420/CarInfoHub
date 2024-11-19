from django import forms
from .models import Car, Comment


class BaseCarForm(forms.ModelForm):
    class Meta:
        model: Car = Car
        exclude: tuple = ('owner', 'slug', 'created_at', 'updated_at')


class CarForm(BaseCarForm):
    pass


class CarUpdateForm(BaseCarForm):
    pass


class CommentForm(forms.ModelForm):
    class Meta:
        model: Comment = Comment
        fields: tuple = ('content',)
