from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^page/', 'clg.views.entry_index'),
    url(r'^cmp/', 'clg.views.autos'),
    url(r'^reg/', 'clg.views.result'),
)
