#-*- encoding: utf-8 -*-

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from account.models import User
from account.serializers import UserIDSerializer, UserInfoSerializer

import urllib, urllib2, json, simplejson
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.middleware.csrf import get_token

import requests
from allauth.socialaccount import providers
from allauth.socialaccount.providers.facebook.provider import FacebookProvider
from allauth.socialaccount.providers.facebook.views import fb_complete_login

from allauth.socialaccount.providers.twitter.provider import TwitterProvider
from allauth.socialaccount.providers.twitter.views import TwitterAPI

from allauth.socialaccount.providers.weibo.provider import WeiboProvider

from allauth.socialaccount.models import (SocialLogin, SocialToken, SocialAccount)
from allauth.socialaccount.helpers import complete_social_login, render_authentication_error

from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate, login, logout
import settings, random

from rest_framework.views import APIView
from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from django.template import RequestContext
from datetime import datetime, timedelta
from django.db.models import Q
import pytz

class UserInfoView(generics.GenericAPIView):
    serializer_class = UserIDSerializer
    permission_classes = (AllowAny, )

    def post(self, request, format=None):
        """
        登入Guest帳號
        """
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            user_id = serializer.data.get('user_id')
            serializer = UserInfoSerializer(User.objects.get(id=user_id))
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


