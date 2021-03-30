import random

from django.contrib.auth.models import User, Group
from django.template.context_processors import request
from rest_framework import permissions, viewsets

from .models import Quiz
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuizSerializer, UserSerializer, GroupSerializer


# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("hello dagger?")


@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    # print(randomQuizs)
    aa = 'quiz'
    new_dict = {aa: randomQuizs}
    print("-1 :: " + str(Quiz.objects.all()))
    print("0 :: " + str(Quiz.objects.filter()))
    print("1 :: " + str(new_dict))
    print("2 :: " + str(randomQuizs))


    serializer = QuizSerializer(randomQuizs, many=True)
    print("3 :: " + str(serializer))
    print("4 :: " + str(QuizSerializer(randomQuizs, many=True)))
    print("5 :: " + str(Quiz))
    print("6 :: " + str(serializer.data))

    return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    # print(queryset)
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# class PostView(viewsets.ModelViewSet):
#     # authentication_classes = (SessionAuthentication, BasicAuthentication)
#     # permission_classes = (IsAuthenticated,)
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # permission_classes = [IsAuthenticated]
#
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     # permission_classes = (permissions.IsAuthenticated,)
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
