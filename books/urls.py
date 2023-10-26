from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all),
    path('<int:id>', views.get_book_by_id),
    path('author/<int:id>', views.get_author_by_id),
    path('author/<int:id>/books', views.get_authors_books_by_id)
]
