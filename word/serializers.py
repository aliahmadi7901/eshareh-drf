from rest_framework import serializers
from .models import Word, CategorizeWord


class CategoryWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorizeWord
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'
