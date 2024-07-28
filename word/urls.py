from django.urls import path, include
from rest_framework.routers import DefaultRouter
from word import views

router = DefaultRouter()
router.register('words', views.WordViewSet, basename='words',)
router.register('categorize', views.WordViewSet, basename='categorize')

urlpatterns = [
    path('', include(router.urls)),
    path('categorize/', include(router.urls)),
    path('create_sentence/?search=<str:word>/', views.CreateSentence.as_view(), name='create_sentence'),
    path('test/', views.Test.as_view(), name='test'),
]
