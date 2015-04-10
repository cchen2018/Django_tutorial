from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # namespace allows django to differentiate URL names if there are multiple apps
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)


