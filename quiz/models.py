from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class Top(models.Model):
#     name = models.TextField(max_length=200)

class Sample2(models.Model):
    quiz = models.CharField(max_length=100, blank=True)


class Quiz(models.Model):
    test = models.ForeignKey(Sample2, related_name='tracks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()
    subtitle = models.CharField(max_length=144, blank=True)

    def __str__(self):
        return f"{self.test}"

# class Post(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=144)
#     subtitle = models.CharField(max_length=144, blank=True)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return '[{}] {}'.format(self.user.username, self.title)
