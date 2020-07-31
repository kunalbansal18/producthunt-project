from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=255)
    url = models.TextField()
    dop =  models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    photo = models.ImageField(upload_to = 'imagesiam/')
    icon = models.ImageField(upload_to = 'imagesiam/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def dop_pretty(self):
        return self.dop.strftime('%b %e %Y')
