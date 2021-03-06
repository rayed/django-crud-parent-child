from django.urls import path

from . import views

app_name = 'books_pc_formset2'

urlpatterns = [
    path('', views.home, name='home'),

    path('person_new', views.person_create, name='person_new'),
    path('person_edit/<int:pk>', views.person_update, name='person_edit'),
    path('person_delete/<int:pk>', views.person_delete, name='person_delete'),

    path('book_new', views.book_create, name='book_new'),
    path('book_edit/<int:pk>', views.book_update, name='book_edit'),
    path('book_delete/<int:pk>', views.book_delete, name='book_delete'),
]
