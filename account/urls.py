
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import patterns, include, url

urlpatterns = format_suffix_patterns(patterns('',
	(r'^', include('allauth.urls')),
))