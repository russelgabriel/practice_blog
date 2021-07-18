"""Defines URL patterns for blogs app"""

from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
	# Home page
	path('', views.index, name='index'),
	# Page for adding new post
	path('new_post/', views.new_post, name='new_post'),
	# Page for editing a post
	path('edit_post/<int:blogpost_id>/', 
		views.edit_post, name='edit_post')
]