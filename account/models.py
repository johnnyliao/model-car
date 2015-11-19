#-*- encoding: utf-8 -*-

from django.contrib.auth.models import AbstractUser

from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from django.contrib.contenttypes import generic

from django.core.exceptions import ObjectDoesNotExist

from django.contrib.sites.models import Site
from datetime import datetime, timedelta
import urlparse, settings

from django.utils import simplejson

STATUS_CHOICES = (
	("guest", u'快速登入'),
	("facebook", u'facebook'),
	("user", u'自建帳號'),
)

class User(AbstractUser):

	def __unicode__(self):
		return self.username


