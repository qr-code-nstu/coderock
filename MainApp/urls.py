from django.urls import path, include
from .views import *

urlpatterns = [
    path('', MainView.as_view()),
    path('user/signin/', UserSignIn.as_view())
]
