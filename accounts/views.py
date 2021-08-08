from django.forms.forms import Form
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .forms import UserCreateForm
from django.views.generic import CreateView

from accounts import forms


# Create your views here.
class Signup(CreateView):
	form_class = UserCreateForm
	success_url = reverse_lazy('accounts:login')
	template_name = 'accounts/signup.html'

