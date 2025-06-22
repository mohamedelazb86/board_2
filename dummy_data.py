import os,django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

import random
from blog.models import Post,Category,Review
from faker import Faker
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile


# job
from job.models import Job,Category,Location,ApplyUser

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
def seed_location(n):
    fake=Faker()
    for _ in range(n):
        Location.objects.create(
            city=fake.name()
        )

def seed_job(n):
    users=User.objects.all()
    jop_type=['Full Time','Part Time']
    category=Category.objects.all()
    location=Location.objects.all()
    images=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
    fake=Faker()
    for _ in range(n):
        Job.objects.create(
            user=users[random.randint(0,len(users)-1)],
            title=fake.name(),
            job_type=jop_type[random.randint(0,1)],
            descriptions=fake.text(max_nb_chars=4000),
            vacany=random.randint(1,100),
            salary=round(random.uniform(5000,50000),2),
            experience=random.randint(1,20),
            image=f'photo_job/{images[random.randint(0,8)]}',
            category=category[random.randint(0,len(category)-1)],
            location=location[random.randint(0,len(location)-1)]


        )
def seed_alluser(n):
    users=User.objects.all()
    jobs=Job.objects.all()
    fake=Faker()
    dummy_cv_content = b'%PDF-1.4\n%Fake CV content for testing.\n%%EOF'
    images=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
    for _ in range(n):
        ApplyUser.objects.create(
            user=users[random.randint(0,len(users)-1)],
            job=jobs[random.randint(0,len(users)-1)],
            name=fake.name(),
            email=fake.email(),
            website=fake.url(),
             cv=SimpleUploadedFile("dummy_cv.pdf",  dummy_cv_content,content_type="application/pdf"),
            image=f'image/{images[random.randint(0,8)]}',

            content=fake.text(max_nb_chars=1000),



        )






# seed_category(200)
# seed_post(750)
# seed_review(750)
# seed_categor_job(120)
# seed_location(100)
# seed_job(250)
seed_alluser(200)

