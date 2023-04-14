from rest_framework import serializers
from .models import Group, Person, Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['title']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'full_name']


class GroupSerializer(serializers.ModelSerializer):
    link = LinkSerializer(read_only=True, many=True)
    class Meta:
        model = Group
        fields = ['name', 'link']