from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db.models.base import Model
from django.views.generic.edit import UpdateView


class UserCreateForm(UserCreationForm):
	fields = ("username", "password1", "password2")
	model = get_user_model()

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].help_text = None		
		self.fields['password1'].help_text = None
		self.fields['password2'].help_text = None
        
