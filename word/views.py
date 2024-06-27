from django.shortcuts import render
from rest_framework import generics

from word.models import Word
from word.serializers import WordSerializer


class WordList(generics.ListAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class WordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class WordCategory(generics.ListAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category_title = self.request.GET['category_title']
        if category_title:
            queryset = queryset.filter(category_title__iexact=category_title)
            return queryset

        return queryset


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
