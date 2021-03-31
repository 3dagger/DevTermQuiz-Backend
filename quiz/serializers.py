from rest_framework import serializers
# from .models import Quiz
from django.contrib.auth.models import User, Group
# from .models import Post
from quiz.models import Quiz, Sample2


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        # fields = '__all__'
        fields = ('title', 'body', 'answer', 'subtitle',)
        # fields = '__all__'


class SampleSerializer(serializers.ModelSerializer):
    # tracks = serializers.StringRelatedField(many=True)
    tracks = QuizSerializer(many=True)

    class Meta:
        model = Sample2
        # fields = '__all__'
        fields = ('tracks',)


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
