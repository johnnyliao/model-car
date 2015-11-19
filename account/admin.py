#-*- encoding: utf-8 -*-
from django import forms

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin, UserChangeForm as DjangoUserChangeForm
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from account.models import User
from salmonella.admin import SalmonellaMixin


class UserAdmin(SalmonellaMixin, DjangoUserAdmin):
	list_display = ['username', 'email']

admin.site.register(User, UserAdmin)
