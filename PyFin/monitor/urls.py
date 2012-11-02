from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'PyFin.monitor.views.home', name='home'),
    url(r'^query$', 'PyFin.monitor.views.query_database', name='query'),
    # url(r'^PyFin/', include('PyFin.foo.urls')),

)
