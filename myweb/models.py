from django.conf import settings
from django.db import models

class Comment(models.Model):
    CommentName = models.CharField(max_length=150,blank=True)
    Comment = models.TextField(max_length=999999,blank=True)

    def __str__(self):
        return f"{self.CommentName} - {self.Comment}"