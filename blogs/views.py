from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import BlogPost
from .forms import PostForm

def index(request):
	"""Home page for blogs"""
	try:
		posts = BlogPost.objects.filter(owner=request.user).order_by('-date_added')
		context = {'posts': posts, 'user': request.user}
		return render(request, 'blogs/index.html', context)
	except:
		context = {'user': request.user}
		return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
	"""Page for creating a new post"""
	if request.method != 'POST':
		form = PostForm()
	else:
		form = PostForm(data=request.POST)
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.owner = request.user
			new_post.save()
			return redirect('blogs:index')

	context = {'form': form}
	return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, blogpost_id):
	post = BlogPost.objects.get(id=blogpost_id)

	if post.owner != request.user:
		raise Http404

	if request.method != 'POST':
		form = PostForm(instance=post)
	else:
		form = PostForm(instance=post, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('blogs:index')

	context = {'form': form, 'post': post}
	return render(request, 'blogs/edit_post.html', context)