from django.db import models
# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField (auto_now_add=True)
    updated_at = models.DateTimeField (auto_now=True)

    def __str__(self):
        return self.title 
    
class user (models.Model):
    username = models.CharField (max_length=30)
    email = models.EmailField ()
    password = models.CharField (max_length=30)
    created_at = models.DateTimeField (auto_now_add=True)
    updated_at = models.DateTimeField (auto_now=True)

    def __str__(self):
        return self.username 