from rest_framework import generics, viewsets
from rest_framework.decorators import action

from word.models import Word, CategorizeWord
from word.permissions import AdminOrReadOnly
from word.serializers import WordSerializer, CategoryWordSerializer


class CategorizeWordViewSet(viewsets.ModelViewSet):
    queryset = CategorizeWord.objects.all()
    serializer_class = CategoryWordSerializer
    permission_classes = (AdminOrReadOnly,)


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = (AdminOrReadOnly,)

    @action(detail=True, methods=['get'])
    def word_category(self, request):
        queryset = Word.objects.all()
        category_title = self.request.query_params.get('category_title')
        if category_title:
            queryset = queryset.filter(categorize_word__title__iexact=category_title)
            return queryset

        return queryset


class CreateSentence(generics.RetrieveAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    lookup_field = 'title'

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.kwargs.get('title')
        if title:
            queryset = queryset.filter(title__iexact=title)
            return queryset

        return queryset


class Test(generics.RetrieveAPIView):
    queryset = Word.objects.order_by("?").first()
    serializer_class = WordSerializer
