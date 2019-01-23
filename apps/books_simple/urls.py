from django.conf.urls import url

from books_simple import views

urlpatterns = [
  url(r'^$', views.home, name='home'),
  url(r'^new$', views.book_create, name='book_new'),
  url(r'^edit/(?P<pk>\d+)$', views.book_update, name='book_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.book_delete, name='book_delete'),
]