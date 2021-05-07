from django.db import models
from users.models import CustomUser
from django.urls import reverse

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_imgs')
    text = models.TextField(max_length=1000)
    added_at = models.TimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def get_absolute_url(self):
        pass
        #return reverse('')
