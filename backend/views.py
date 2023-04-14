from rest_framework import generics
from .models import Group, Person
from .serializers import GroupSerializer, PersonSerializer


class PersonCreateAPIView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class GroupAPIView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupFilterAPIView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer