from rest_framework import serializers

from deaf.models import Sentence, CategoriesOfTheDeaf


class CategoryOfTheDeafSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesOfTheDeaf
        fields = '__all__'


class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = '__all__'
