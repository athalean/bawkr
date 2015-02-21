from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from bawkr.views import Bawks

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'realtime_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='test.html')),
    url(r'^bawks$', Bawks.as_view()),
)
