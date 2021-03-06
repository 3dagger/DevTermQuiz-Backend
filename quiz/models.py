from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()
    subtitle = models.CharField(max_length=144, blank=True)

    # def __str__(self):
    #     return '[{}] {}'.format(self.user.username, self.title)

# class Post(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=144)
#     subtitle = models.CharField(max_length=144, blank=True)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return '[{}] {}'.format(self.user.username, self.title)

