from django.conf.urls import url, include
import debug_toolbar
from . import views

urlpatterns = [
    url(r'^debug/', include(debug_toolbar.urls)),
    url(r'^author/$', views.author_update, name='author_new'),
    url(r'^author/(?P<author_id>[0-9]+)/$', views.author_update, name='author_update'),
]
