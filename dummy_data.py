import os,django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

import random
from blog.models import Post,Category,Review
from faker import Faker
from django.contrib.auth.models import User

# job
from job.models import Job,Category

def seed_category(n):
    fake=Faker()
    for _ in range(n):
        Category.objects.create(
            name=fake.name()


        )
def seed_post(n):
    fake=Faker()
    user=User.objects.all()
    category=Category.objects.all()
    images=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
    for _ in range(n):
        Post.objects.create(
            user=user[random.randint(0,len(user)-1)],
            title=fake.name(),
            content=fake.text(max_nb_chars=3000),
            image=f'photo_post/{images[random.randint(0,8)]}',
            category=category[random.randint(0,len(category)-1)],


        )
def seed_review(n):
    fake=Faker()
    user=User.objects.all()
    posts=Post.objects.all()
    for _ in range(n):
        Review.objects.create(
            user=user[random.randint(0,len(user)-1)],
            post=posts[random.randint(0,len(posts)-1)],
            content=fake.text(max_nb_chars=1000),
            rate=random.randint(1,6)
        )

def seed_categor_job(n):
    fake=Faker()
    for _ in range(n):
        Category.objects.create(
            name=fake.name()

        )
# seed_category(200)
# seed_post(750)
# seed_review(750)
seed_categor_job(5)

