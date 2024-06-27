from django.urls import path

from word import views

urlpatterns = [
    path('', views.WordList.as_view(), name='word_list'),
    path('word/<int:pk>/', views.WordDetail.as_view(), name='word_detail'),
    path('category/<str:category_title>/', views.WordCategory.as_view(), name='word_category'),
    path('create_sentence/?search=<str:word>/', views.CreateSentence.as_view(), name='create_sentence'),
    path('test/', views.Test.as_view(), name='test'),
]
