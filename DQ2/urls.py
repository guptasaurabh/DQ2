from django.conf.urls import patterns, include, url
from DQ2.views import hello,current_datetime
from digiquiz.views import createQuiz,bhai
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    # Examples:
    # url(r'^$', 'DQ2.views.home', name='home'),
    # url(r'^DQ2/', include('DQ2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^createquiz$', createQuiz),
     url(r'^bhai$', bhai),
     url(r'^logout/$', 'django.contrib.auth.views.logout', name='auth_logout'),
    
)
