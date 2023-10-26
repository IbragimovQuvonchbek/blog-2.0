from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE   
    )
    body = RichTextField()
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('full_post', args=[str(self.pk)])