from django.conf.urls import include, url
from django.contrib import admin

import books_simple.urls
import books_pc_formset.urls
import books_pc_formset2.urls
import books_pc_multi_view.urls
import apps.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^books_simple/', include(books_simple.urls, namespace='books_simple')),
    url(r'^books_pc_formset/', include(books_pc_formset.urls, namespace='books_pc_formset')),
    url(r'^books_pc_formset2/', include(books_pc_formset2.urls, namespace='books_pc_formset2')),
    url(r'^books_pc_multi_view/', include(books_pc_multi_view.urls, namespace='books_pc_multi_view')),
    url(r'^$', apps.views.home, name='home'),
]
