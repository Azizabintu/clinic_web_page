from django.db import models


class Worker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    information = models.TextField()
    photo = models.ImageField(default="default_profile_pic.jpg")


