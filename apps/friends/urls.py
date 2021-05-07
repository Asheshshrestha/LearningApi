from django.urls import path
from .views import FriendsCreateApi,FriendsListApi,FriendsUpdateApi
urlpatterns = [

    path('create',FriendsCreateApi.as_view()),
    path('list',FriendsListApi.as_view()),
    path('<int:pk>',FriendsUpdateApi.as_view())

]