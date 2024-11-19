from rest_framework import serializers
from .models import Car, Comment


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model: Car = Car
        fields: str = '__all__'
        read_only_fields: tuple = ('slug', 'owner')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model: Comment = Comment
        fields: str = '__all__'
        read_only_fields: tuple = ('author', 'car')

