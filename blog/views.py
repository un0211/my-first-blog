from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def main(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts}) #request와 템플릿을 받아 내용이 리턴 브러우저로

def intro(request):
	return render(request, 'blog/intro.html', {}) #request와 템플릿을 받아 내용이 리턴 브러우저로

def intro_task(request):
	return render(request, 'blog/intro_task.html', {}) #request와 템플릿을 받아 내용이 리턴 브러우저로

def notice(request):
	return render(request, 'blog/notice.html', {}) #request와 템플릿을 받아 내용이 리턴 브러우저로

def qna(request):
	return render(request, 'blog/qna.html', {}) #request와 템플릿을 받아 내용이 리턴 브러우저로

def login(request):
	return render(request, 'blog/login.html', {}) #request와 템플릿을 받아 내용이 리턴 브러우저로

def login(request):
	return render(request, 'blog/logout.html', {}) #request와 템플릿을 받아 내용이 리턴 브러우저로

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts}) #request와 템플릿을 받아 내용이 리턴 브러우저로

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form':form})