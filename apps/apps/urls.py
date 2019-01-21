from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

import theme.views
import books_simple.urls
import books_pc_formset.urls
import books_pc_formset2.urls
import books_pc_multi_view.urls
import books_pc_multi_view2.urls

urlpatterns = [
    url(r'^$', theme.views.home, name='home'),
    url(r'^books_simple/', include((books_simple.urls, 'books_simple'), namespace='books_simple')),
    url(r'^books_pc_formset/', include((books_pc_formset.urls, 'books_pc_formset'), namespace='books_pc_formset')),
    url(r'^books_pc_formset2/', include((books_pc_formset2.urls, 'books_pc_formset2'), namespace='books_pc_formset2')),
    url(r'^books_pc_multi_view/', include((books_pc_multi_view.urls, 'books_pc_multi_view'), namespace='books_pc_multi_view')),
    url(r'^books_pc_multi_view2/', include((books_pc_multi_view2.urls, 'books_pc_multi_view2'), namespace='books_pc_multi_view2')),
    path('admin/', admin.site.urls),
]
