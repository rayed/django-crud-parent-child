from django.urls import path

from . import views

app_name = 'books_pc_multi_view'

urlpatterns = [
    path('', views.home, name='home'),

    path('book_view/<int:pk>/', views.book_view, name='book_view'),
    path('book_new', views.book_create, name='book_new'),
    path('book_edit/<int:pk>/', views.book_update, name='book_edit'),
    path('book_delete/<int:pk>/', views.book_delete, name='book_delete'),

    path('review_new/<int:parent_pk>/', views.review_create, name='review_new'),
    path('review_edit/<int:pk>/', views.review_update, name='review_edit'),
    path('review_delete/<int:pk>/', views.review_delete, name='review_delete'),
]
