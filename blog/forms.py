from django import forms

from .models import Post

class PostForm(forms.ModelForm): #이 폼이 ModelForm이란 걸 알려줌
	class Meta:
		model = Post
		fields = ('title', 'text',)