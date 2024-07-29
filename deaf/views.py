from django.shortcuts import render
from rest_framework import generics

from deaf.models import Sentence
from deaf.serializers import SentenceSerializer


class SentenceList(generics.ListAPIView):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer


class SentenceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer


class SentenceCategoryList(generics.ListAPIView):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category_title = self.request.query_params.get('category_title')
        if category_title:
            queryset = queryset.filter(category_title__icontains=category_title)
            return queryset

        return queryset
