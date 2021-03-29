from rest_framework import serializers
# from .models import Quiz
from django.contrib.auth.models import User, Group
# from .models import Post
from quiz.models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'body', 'answer', 'subtitle')

    # class Meta:
    #     model = User
    #     fields = ('id', 'username', 'email')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# class PostSerializer(serializers.ModelSerializer):
#     user = QuizSerializer(read_only=True)
#
#     class Meta:
#         model = Post
#         fields = (
#             'id',
#             'user',
#             'title',
#             'subtitle',
#             'content',
#             'created_at',
#         )
#         read_only_fields = ('created_at',)
