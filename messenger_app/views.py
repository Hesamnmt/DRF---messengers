from django.shortcuts import render
from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer


class MessageView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer