from django.shortcuts import render
from.models import Post 
from django.views.generic import View
from .forms import PostForm

class PostView(View):
	def get(self,request):
		template='posts/todos.html'
		posts=Post.objects.all()
		form=PostForm()
		context={
		'posts':posts,
		'form':form,
		}
		return render(request,template,context)

	
