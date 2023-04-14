from django.db import models


class Person(models.Model):
    id = models.CharField(max_length=221, primary_key=True)
    full_name = models.CharField(max_length=221)


class Link(models.Model):
    title = models.CharField(max_length=221)


class Group(models.Model):
    name = models.CharField(max_length=221)
    link = models.ManyToManyField(Link)