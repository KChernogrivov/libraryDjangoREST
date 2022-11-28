from django.urls import path, include
from . import views

urlpatterns = [
    path(r'auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.authtoken')),

    path('books/create/', views.BookCreate.as_view()),
    path('books/', views.BookListView.as_view()),
    path('books/<int:pk>/', views.book_detail),

    path('authors/', views.author_list),
    path('authors/create/', views.AuthorCreate.as_view()),
    path('authors/<int:pk>/', views.author_detail),
]