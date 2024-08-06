from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

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
    users = User.objects.get(id = pk)

    #convert to python dictionary
    serializer = UserSerializer(users)

    #Dictionay render to json
    json_data = JSONRenderer().render(serializer.data)

    #json sent to user
    return HttpResponse(json_data, content_type = "application/json")

#View for deserialization 
@csrf_exempt
def user_create(request):
    
    if request.method == 'POST':
        json_data = request.body

        # JSON to Stream
        print("This is json Body from User End", json_data)

        stream = io.BytesIO(json_data)

        # Streat to python
        pythonData = JSONParser().parse(stream)
        
        print("This is user id:", pythonData["user_id"])

        # Python to complex data
        serializer = UserSerializer(data = pythonData)

        if serializer.is_valid():
            serializer.save()
            res = {
                "message": "Successfully inserted data"
            }
            js_data = JSONRenderer().render(res)
            return HttpResponse(js_data, content_type = "application.json")
        else:
            js_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(js_data, content_type = "application.json")
        
    elif request.method == "PUT":
        json_data = request.body

        #json to stream
        stream = io.BytesIO(json_data)

        #stream to python
        pythonData = JSONParser().parse(stream)

        user_id = pythonData.get('user_id')
        user = User.objects.get(user_id = user_id)

        serializer = UserSerializer(user, data=pythonData, partial = True)

        if serializer.is_valid():
            serializer.save()
            res = {
                "message": "Successfully Updated data"
            }
            js_data = JSONRenderer().render(res)
            return HttpResponse(js_data, content_type = "application.json")
        else:
            js_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(js_data, content_type = "application.json")
