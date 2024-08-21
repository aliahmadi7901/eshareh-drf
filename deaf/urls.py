from django.urls import path, include
from rest_framework import routers

from deaf import views

router = routers.DefaultRouter()
router.register('', views.CategoryOfTheDeafView, basename='category_of_the_deaf')

urlpatterns = [
    path('', views.SentenceListView.as_view(), name='sentence-list'),
    path('sentence/<int:pk>/', views.SentenceDetailView.as_view(), name='sentence-detail'),
    path('sentence-category/<str:category_title>/', views.SentenceCategoryListView.as_view(), name='category-list'),
    path('category-of-the-deaf/', include(router.urls))
]
