from django.shortcuts import render ,HttpResponse
from blog.models import Post

# Create your views here.


def bloghome(request):
	allPosts= Post.objects.all()
	context={'allPosts': allPosts}

	return render(request,'blog/blogHome.html',context)



def blogpost(request ,slug):
	post = Post.objects.filter(slug=slug).first()
	#post = Post.objects.get(slug=slug)
	context = {'post': post }
	return render(request,'blog/blogPost.html',context)



from django.contrib.auth.models import User
from blog.serializers import PostSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	#permission_classes = [IsAdminUser]

