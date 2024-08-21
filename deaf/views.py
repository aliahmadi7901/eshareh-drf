from rest_framework import generics, viewsets

from deaf.models import Sentence, CategoriesOfTheDeaf
from deaf.serializers import SentenceSerializer, CategoryOfTheDeafSerializer
from word.permissions import AdminOrReadOnly


class CategoryOfTheDeafView(viewsets.ModelViewSet):
    queryset = CategoriesOfTheDeaf.objects.all()
    serializer_class = CategoryOfTheDeafSerializer
    permission_classes = (AdminOrReadOnly,)


class SentenceListView(generics.ListCreateAPIView):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer
    permission_classes = (AdminOrReadOnly,)


class SentenceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer
    permission_classes = (AdminOrReadOnly,)


class SentenceCategoryListView(generics.ListAPIView):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer
    permission_classes = (AdminOrReadOnly,)

    def get_queryset(self):
        queryset = super().get_queryset()
        category_title = self.kwargs.get('category_title')
        if category_title:
            queryset = queryset.filter(category__title=category_title)
            return queryset

        return queryset
