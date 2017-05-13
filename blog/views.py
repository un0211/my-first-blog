from django.shortcuts import render

# Create your views here.
def post_list(request):
	return render(request, 'blog/post_list.html', {}) #request와 템플릿을 받아 내용이 리턴 브러우저로