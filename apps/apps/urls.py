from django.conf.urls import include, url
from django.contrib import admin

import books_cbv.urls
import books_fbv.urls
import books_fbv_user.urls
import apps.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^books_cbv/', include(books_cbv.urls, namespace='books_cbv')),
    url(r'^books_fbv/', include(books_fbv.urls, namespace='books_fbv')),
    url(r'^books_fbv_user/', include(books_fbv_user.urls, namespace='books_fbv_user')),
    url(r'^$', apps.views.home),
]
