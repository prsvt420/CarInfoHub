from django import forms
from .models import Car, Comment


class BaseCarForm(forms.ModelForm):
    class Meta:
        model: Car = Car
        exclude: tuple = ('slug', 'created_at', 'updated_at')


class CarForm(BaseCarForm):
    pass


class CarUpdateForm(BaseCarForm):
    class Meta(BaseCarForm.Meta):
        exclude: tuple = BaseCarForm.Meta.exclude + ('owner',)


class CommentForm(forms.ModelForm):
    class Meta:
        model: Comment = Comment
        fields: tuple = ('content',)
