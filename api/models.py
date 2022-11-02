
from django.db import models
from users.models import User

class Articles(models.Model):
    name = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)
    avtor = models.CharField(max_length=1000)
    src = models.FileField(upload_to='media/articles')
    file = models.FileField(upload_to='media/articles')

class Books(models.Model):

    name = models.CharField(max_length=1000)
    src = models.FileField(upload_to='media/books/src')
    # type1 = models.CharField(max_length=155)
    date = models.CharField(max_length=1000)
    file = models.FileField(upload_to='media/books/file')
    avtor = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)

class Documents(models.Model):
    name = models.CharField(max_length=1000)
    src = models.FileField(upload_to='media/documents/src')
    date = models.CharField(max_length=1000)
    file = models.FileField(upload_to='media/documents/file')
    avtor = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)

class Events(models.Model):
    name = models.CharField(max_length=1000)
    src = models.FileField(upload_to='media/events/src')
    date = models.CharField(max_length=1000)
    file = models.FileField(upload_to='media/events/file')
    avtor = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)



class News(models.Model):
    CHOICES = (
        ('1', 'DKFMKSOMS'),
        ('1', 'DKFMKSOMS'),
        ('1', 'DKFMKSOMS'),
        ('1', 'DKFMKSOMS'),
    )
    name = models.CharField(max_length=1000)
    src = models.FileField(upload_to='media/events/src')
    date = models.CharField(max_length=1000)
    file = models.FileField(upload_to='media/events/file')
    avtor = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)

class Courses(models.Model):
    name = models.CharField(max_length=1000)
    src = models.FileField(upload_to='media/courses/src')
    date = models.CharField(max_length=1000)
    file = models.FileField(upload_to='media/courses/file')
    avtor = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)
    comment = models.TextField()


class Videos(models.Model):
    name = models.CharField(max_length=1000)
   
    file = models.FileField(upload_to='media/videos/file')
    date = models.CharField(max_length=1000)
    avtor = models.CharField(max_length=1000)
    

class Group(models.Model):
    name = models.CharField(max_length=1000)
    chat = models.CharField(max_length=1000, null=True, blank=True)
    avtor = models.CharField(max_length=1000)
    file = models.FileField()


class Sms(models.Model):
    text = models.TextField(max_length=1000)
    group = models.ManyToManyField(Group)
    date = models.CharField(max_length=1000, null=True, blank=True)
    user = models.CharField(max_length=1000, null=True, blank=True)
    fio = models.CharField(max_length=1000)


class GroupUser(models.Model):
    user_id = models.CharField(max_length=1000)
    group_id = models.CharField(max_length=1000)
