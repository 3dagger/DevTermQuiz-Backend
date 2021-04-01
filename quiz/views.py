import random

from django.contrib.auth.models import User, Group
from django.template.context_processors import request
from rest_framework import permissions, viewsets

from .models import Quiz, Sample2
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuizSerializer, UserSerializer, GroupSerializer, SampleSerializer


# Create your views here.

@api_view(['GET'])
def helloAPI(request):
    sample = Sample2.objects.filter()
    serializer = SampleSerializer(sample, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    aa = 'quiz'
    new_dict = {aa: randomQuizs}
    print("-1 :: " + str(Quiz.objects.all()))
    print("0  :: " + str(Quiz.objects.filter()))
    print("1  :: " + str(new_dict))
    print("2  :: " + str(randomQuizs))

    serializer = QuizSerializer(randomQuizs, many=True)
    print("3  :: " + str(serializer))
    print("4  :: " + str(QuizSerializer(randomQuizs, many=True)))
    print("5  :: " + str(Quiz))
    print("6  :: " + str(serializer.data))

    return Response(serializer.data)


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.filter().order_by('?')[:1]
    print(Quiz.objects.all())
    serializer_class = QuizSerializer


class helloViewSet(viewsets.ModelViewSet):
    queryset = Sample2.objects.all()
    print("HelloViewSet")
    serializer_class = SampleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
