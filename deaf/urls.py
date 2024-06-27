from django.urls import path

from deaf import views

urlpatterns = [
    path('', views.SentenceList.as_view(), name='sentence-list'),
    path('sentence/<int:pk>/', views.SentenceDetail.as_view(), name='sentence-detail'),
    path('category/<str:category_title>/', views.SentenceCategoryList.as_view(), name='category-list'),

]
