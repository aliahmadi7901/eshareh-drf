from django.urls import path

from word import views

urlpatterns = [
    path('', views.WordList.as_view(), name='word_list'),
    path('word/<int:pk>/', views.WordDetail.as_view(), name='word_detail'),
    path('<str:category_title>/', views.WordCategory.as_view(), name='word_category'),
]
