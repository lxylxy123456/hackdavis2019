from django.contrib import admin
from django.conf.urls import include, url

from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^static/(?P<path>.*)$', serve, settings.STATIC_DICT),
    url(r'^media/(?P<path>.*)$', serve, settings.MEDIA_DICT),

	url(r'^', include('sch_account.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
