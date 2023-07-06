from django.db import models
from datetime import date

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

class Blog(models.Model):
    name = models.CharField(max_length=200) #Blog El Invierno Sovietico (ejemplo)
    tagline = models.TextField() #Las terribles historias de la invasion nazi a la USSR.

    def __str__(self) -> str:
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name
    
class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.headline