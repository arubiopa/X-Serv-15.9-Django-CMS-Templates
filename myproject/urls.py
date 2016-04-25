from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout$', 'django.contrib.auth.views.logout'),
    url(r'^annotated/css/(?P<path>.*)$','django.views.static.serve',
    	{'document_root': settings.STATIC2_URL}),
   	url(r'^annotated/(.*)$','cms.views.cms_annotated'),
    url(r'^(.*$)','cms.views.cms'),
)
