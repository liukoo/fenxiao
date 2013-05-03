import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fenxiao.views.home', name='home'),
    # url(r'^fenxiao/', include('fenxiao.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^add/$', 'fenxiao.agent.views.add'),
    (r'^$', 'fenxiao.agent.views.index'),
)
urlpatterns += staticfiles_urlpatterns()
