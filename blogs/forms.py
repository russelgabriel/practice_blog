from django import forms
from .models import BlogPost

class PostForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['title', 'text']
		labels = {'title': '', 'text': ''}
		help_texts = {'title': 'Title of the post', 'text': 'Body of the post'}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}