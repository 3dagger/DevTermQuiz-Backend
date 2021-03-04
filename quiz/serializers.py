from rest_framework import serializers
# from .models import Quiz
from django.contrib.auth.models import User
from .models import Post


class QuizSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = Quiz
    #     fields = ('title', 'body', 'answer', 'subtitle')

    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class PostSerializer(serializers.ModelSerializer):
    user = QuizSerializer(read_only=True)


    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'subtitle',
            'content',
            'created_at',
        )
        read_only_fields = ('created_at',)