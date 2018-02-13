from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite import settings
from account.views import account_registration_page
from account.views import account_login_page
from account.views import account_logout_page
print '**********'
urlpatterns = patterns('',
	url(r'^login/$',account_login_page, name='account_login'),
    url(r'^registration/$',account_registration_page, name='account_registration'),
    url(r'^logout/$',account_logout_page, name='account_logout'),
    
)
