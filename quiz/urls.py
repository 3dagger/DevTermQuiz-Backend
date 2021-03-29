from django.urls import path, include
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
# from .views import PostView
# from .views import helloAPI, randomQuiz
from quiz import views
from quiz.views import randomQuiz, helloAPI

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomQuiz),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# post_list = PostView.as_view({
#     'post': 'create',
#     'get': 'list'
# })
#
# post_detail = PostView.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# urlpatterns = format_suffix_patterns([
#     path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('posts/', post_list, name='post_list'),
    # path('posts/<int:pk>/', post_detail, name='post_detail'),
# ])