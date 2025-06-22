from django.db import models


class Home(models.Model):
    name=models.CharField(max_length=120)
    descriptions=models.TextField(max_length=3500)
    email=models.CharField(max_length=75)
    image=models.ImageField(upload_to='photo_commpany')
    phone=models.CharField(max_length=25)
    address=models.CharField(max_length=120)
    facebook=models.URLField(null=True,blank=True)
    twitter=models.URLField(null=True,blank=True)
    instgram=models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name
