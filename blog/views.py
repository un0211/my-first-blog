from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts}) #request와 템플릿을 받아 내용이 리턴 브러우저로

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})