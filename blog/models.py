from django.db import models

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()
