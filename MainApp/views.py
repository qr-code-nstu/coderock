from django.shortcuts import render
from django.views import View
from .models import *
from .serializers import *
from rest_framework.generics import *


class MainView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer




# Create your views here.
