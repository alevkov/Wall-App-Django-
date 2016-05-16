import json

from wallapp.models import User, WallPost

from django.contrib.auth import login, authenticate

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.core.mail import send_mail


@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    username = data['username']
    password = data['password']
    user = authenticate(username=username, password=password)
    if user is not None:

        content = {"username": user.username, "age": user.age, "sex": user.sex}
        return Response(content, status=status.HTTP_200_OK)
    else:
        print "not done"
        return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def register(request):
    data = JSONParser().parse(request)
    user = User.objects.create_user(data['username'],
                                 age=data['age'],
                                 sex=data['sex'],
                                 password=data['password'])
    email_subject = 'Account creation'
    email_body = "Hey %s, you have just signed up for The Wall. Enjoy!" % (user.username)
    print data
    send_mail(email_subject, email_body, 'aquifi.scanner@gmail.com', [data['email']], fail_silently=False)
    return Response(status=status.HTTP_200_OK)


# POSTS

@api_view(['GET'])
def get_wall(request):
    set = WallPost.objects.all()
    print set.values()
    results = [obj.as_json() for obj in set]

    return Response(results, status=status.HTTP_200_OK)

@api_view(['POST'])
def write(request):
    data = JSONParser().parse(request)
    text = data["text"]
    poster_name = data["poster"]
    if text is not None:
        post = WallPost(text=text, poster=User.objects.get(username=poster_name))
        post.save()
        return Response(status=status.HTTP_200_OK)
    else:
        Response(status=status.HTTP_403_FORBIDDEN)
