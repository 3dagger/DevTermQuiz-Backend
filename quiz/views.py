import random

# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Quiz
# from .serializers import QuizSerializer
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework import permissions

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# @api_view(['GET'])
# def helloAPI(request):
#     return Response("hello dagger?")
#
#
# @api_view(['GET'])
# def randomQuiz(request, id):
#     totalQuizs = Quiz.objects.all()
#     randomQuizs = random.sample(list(totalQuizs), id)
#     serializer = QuizSerializer(randomQuizs, many=True)
#     return Response(serializer.data)


class PostView(viewsets.ModelViewSet):
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
