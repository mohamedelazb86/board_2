from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


JOB_TYPE=[
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
    ]

class Job(models.Model):
    user=models.ForeignKey(User,related_name='job_user',on_delete=models.CASCADE)
    title=models.CharField(max_length=120)
    job_type=models.CharField(max_length=100,choices=JOB_TYPE)
    descriptions=models.TextField(max_length=5000)
    publish_date=models.DateTimeField(default=timezone.now)
    vacany=models.IntegerField()
    salary=models.FloatField()
    experience=models.IntegerField()
    image=models.ImageField(upload_to='photo_job')
    slug=models.SlugField(null=True,blank=True)
    category=models.ForeignKey('Category',related_name='job_category',on_delete=models.SET_NULL,null=True,blank=True)
    location=models.ForeignKey('Location',related_name='job_location',on_delete=models.SET_NULL,null=True,blank=True)


    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Job,self).save(*args,**kwargs)



class Category(models.Model):
    name=models.CharField(max_length=120)

    def __str__(self):
        return self.name
    
class Location(models.Model):
    city=models.CharField(max_length=120)

    def __str__(self):
        return self.city
