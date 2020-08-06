from django.urls import path

from . import views

app_name = 'book'
urlpatterns = [
    path('', views.BookListView.as_view(), name='list'),
    path('create/', views.BookCreateView.as_view(), name='create'),
    path('update/<int:id>/', views.BookUpdateView.as_view(), name='update'),
]
