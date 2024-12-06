from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.fullname

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    story = models.TextField()

    def __str__(self):
        return self.name