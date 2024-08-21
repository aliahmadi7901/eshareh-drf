from django.urls import path, include
from rest_framework.routers import DefaultRouter
from word import views

router = DefaultRouter()
router.register('categorize', views.CategorizeWordViewSet, basename='categorize')
router.register('words', views.WordViewSet, basename='words',)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('create_sentence/<str:title>/', views.CreateSentence.as_view(), name='create_sentence'),
    path('test/', views.Test.as_view(), name='test'),
]
