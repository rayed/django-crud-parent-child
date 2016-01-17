from django.conf.urls import include, url
from django.contrib import admin

import books_cbv.urls
import books_fbv.urls
import books_fbv_user.urls
import books_pc_formset.urls
import books_pc_formset2.urls
import apps.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^books_cbv/', include(books_cbv.urls, namespace='books_cbv')),
    url(r'^books_fbv/', include(books_fbv.urls, namespace='books_fbv')),
    url(r'^books_fbv_user/', include(books_fbv_user.urls, namespace='books_fbv_user')),
    url(r'^books_pc_formset/', include(books_pc_formset.urls, namespace='books_pc_formset')),
    url(r'^books_pc_formset2/', include(books_pc_formset2.urls, namespace='books_pc_formset2')),
    url(r'^$', apps.views.home),
]
