from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from word.models import Word, CategorizeWord
from word.serializers import WordSerializer, CategoryWordSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    @action(detail=True, methods=['get'])
    def word_category(self, request):
        queryset = Word.objects.all()
        category_title = self.request.GET['category_title']
        if category_title:
            queryset = queryset.filter(categorize_word__title__iexact=category_title)
            return queryset

        return queryset


class CategorizeWordViewSet(viewsets.ModelViewSet):
    queryset = CategorizeWord.objects.all()
    serializer_class = CategoryWordSerializer


class CreateSentence(generics.RetrieveAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.query_params.get('search')
        if title:
            queryset = queryset.filter(title__iexact=title)
            return queryset

        return queryset


class Test(generics.RetrieveAPIView):
    queryset = Word.objects.order_by("?").first()
    serializer_class = WordSerializer
