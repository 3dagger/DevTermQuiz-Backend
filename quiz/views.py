import random

from .models import Quiz
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuizSerializer


# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("hello dagger?")


@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomQuizs, many=True)
    return Response(serializer.data)

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
