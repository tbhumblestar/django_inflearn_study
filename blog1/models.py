from django.conf import settings
from django.db import models

# Create your models here.
#models.py

class Post(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False,verbose_name="공개여부")
    photo = models.ImageField(blank=True,upload_to="instagram/post/%Y/%M")

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    message=models.TextField()

