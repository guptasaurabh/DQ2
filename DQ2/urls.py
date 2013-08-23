from django.conf.urls import patterns, include, url
from DQ2.views import hello,current_datetime
from digiquiz.views import createQuiz,login,logout,getsubdept,testajax,addsection,addsec,quiz,addquestions,testModule
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^getdept',getsubdept),
    # Examples:
    # url(r'^$', 'DQ2.views.home', name='home'),
    # url(r'^DQ2/', include('DQ2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^createquiz$', createQuiz),
     url(r'^logout$',logout,name='logout'),
     url(r'^login$',login),
     url(r'^testajax$',testajax), 
     url(r'^getsubdept$',getsubdept), 
     url(r'^addsection/(.*)',addsection),
     url(r'^addsec$',addsec),
     url(r'^quiz/(.*)',quiz),
     url(r'^addquestion/(.*)',addquestions),
     url(r'^test$',testModule),
     
     
)
