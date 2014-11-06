# coding: utf-8
from django.shortcuts import render
from apps.userprofile.models import  UserProfile
from django.views.generic import ListView,CreateView,DeleteView,UpdateView

# Create your views here.


class UserProfileList(ListView):
	model = UserProfile


class UserProfileCreate(CreateView):
	model = UserProfile
	success_url = '/'