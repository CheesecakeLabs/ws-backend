from django.db import models


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=255)
	text = models.TextField()
	created_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title