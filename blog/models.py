from django.db import models
from taggit.managers import TaggableManager

from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify




class Post(models.Model):
    user=models.ForeignKey(User,related_name='post_user',on_delete=models.CASCADE)
    title=models.CharField(max_length=120)
    content=models.TextField(max_length=3500)
    image=models.ImageField(upload_to='photo_post')
    draft=models.BooleanField(default=True)
    tags = TaggableManager()
    slug=models.SlugField(null=True,blank=True)
    publish_date=models.DateTimeField(default=timezone.now)
    category=models.ForeignKey('Category',related_name='post_category',on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Post,self).save(*args,**kwargs)


class Category(models.Model):
    name=models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Review(models.Model):
    user=models.CharField(max_length=120)
    post=models.ForeignKey(Post,related_name='review_post',on_delete=models.CASCADE)
    publish_date=models.DateTimeField(default=timezone.now)
    content=models.TextField(max_length=1500)
    rate=models.IntegerField(choices=[(i,i) for i in range(1,6)])

    def __str__(self):
        return str(self.post)

