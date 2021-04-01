from rest_framework import serializers
from django.contrib.auth.models import User, Group
from quiz.models import Quiz, Sample2


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'body', 'answer', 'subtitle',)


class SampleSerializer(serializers.ModelSerializer):
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

