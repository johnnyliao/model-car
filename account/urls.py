
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import patterns, include, url

from account.views import *

urlpatterns = format_suffix_patterns(patterns('',
	url('^user_info/', UserInfoView.as_view()),
))