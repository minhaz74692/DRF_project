from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.

#Queryset
def users_list(request):

    #complex data
    users = User.objects.all()

    #convert to python dictionary
    serializer = UserSerializer(users, many = True)

    #Dictionay render to json
    json_data = JSONRenderer().render(serializer.data)

    #json sent to user
    return HttpResponse(json_data, content_type = "application/json")

#Single user instance (Find user via user id)
def user_info(request, pk): # Here pk means Primary Key

    #complex data
    users = User.objects.get(user_id = pk)

    #convert to python dictionary
    serializer = UserSerializer(users,)

    #Dictionay render to json
    json_data = JSONRenderer().render(serializer.data)

    #json sent to user
    return HttpResponse(json_data, content_type = "application/json")

