from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializers
from .models import Todo
# Create your views here.
class TodoView(viewsets.ModelViewSet):       # add this
    serializer_class = TodoSerializers          # add this
    queryset = Todo.objects.all() 
