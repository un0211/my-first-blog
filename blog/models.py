from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):  # Post란 객체. django Model임을 알려줌. Post가 django database에 저장되어야 한다.
	author = models.ForeignKey('auth.User') # 다른 모델 참고
	title = models.CharField(max_length=200) #글자수 제한할 때 씀
	text = models.TextField() #글자수 제한 X
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title