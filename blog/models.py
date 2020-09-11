from django.db import models

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50] + ('...')

    def pub_date_refined(self):
        return self.pub_date.strftime('%b %w, %Y')
        #https://strftime.org/
        #https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
