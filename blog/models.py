from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Blogs"

class Discussion(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    content=models.TextField()
    
    def __str__(self):
        return self.title
class Meta:
        verbose_name_plural = "services"