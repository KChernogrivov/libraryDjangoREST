from django.urls import path, include
from . import views

urlpatterns = [
    path(r'auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.authtoken')),

    path('books/create', views.BookCreate.as_view()),
    path('books/', views.book_list),
    path('books/<int:pk>/', views.book_detail),

    path('authors/', views.author_list),
    path('authors/<int:pk>/', views.author_detail),
]