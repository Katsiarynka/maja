from django.db import models


class Creator(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(max_length=100)
    bio = models.TextField()
    twitter = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    tiktok = models.CharField(max_length=100)
    creator_nickname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    volume = models.IntegerField(default=0)
    quantity_sold = models.IntegerField(default=0)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
