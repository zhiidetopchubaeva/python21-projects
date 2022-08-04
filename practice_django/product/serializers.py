from rest_framework import serializers

from .models import Category, Product
from review.models import Review
from review.serializers import ReviewSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['reviews'] = ReviewSerializer(instance.reviews.all(), many=True).data

        return repr

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'