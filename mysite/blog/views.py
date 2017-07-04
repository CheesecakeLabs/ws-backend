from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

import json

def index(request):
	return render(request, 'index.html')

def blog(request):
	all_posts = Post.objects.all()
	return render(request, 'blog.html', {'posts': all_posts})

def post(request, pk):
	post = Post.objects.get(id=pk)
	return render(request, 'post.html', {'post': post})

def api_posts(request):
	response = []
	for p in Post.objects.all():
		response.append({
			'title':p.title,
			'text': p.text,
			'author':p.author.email,
			'created_at':str(p.created_at)
		})

	return HttpResponse(json.dumps(response))

