from rest_framework.serializers import *
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)


class ExecutorSerializer(ModelSerializer):
    id = UserSerializer()

    class Meta:
        model = Executor
        fields = ('id', 'first_name', 'second_name', 'last_name',
                  'image', 'phone', 'about')


class ClientSerializer(ModelSerializer):
    id = UserSerializer()

    class Meta:
        model = Client
        fields = ('id', 'first_name', 'second_name', 'last_name',
                  'image', 'phone', 'about')


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        field = '__all__'
