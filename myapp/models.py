from django.db import models

DIVISION_CHOICE=[
    ('Dhaka', 'Dhaka'),
    ('Chattogram', 'Chattogram'),
    ('Rajshahi', 'Rajshahi'),
    ('Sylhet', 'Sylhet'),
    ('Barisal', 'Barisal'),
    ('Rangpur', 'Rangpur'),
    ('Khulna', 'Khulna'),
    ('Mymensingh', 'Mymensingh'),
]

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False, auto_now_add=False)
    gender=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    pin=models.PositiveIntegerField()
    division=models.CharField(choices=DIVISION_CHOICE, max_length=50)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    job_city=models.CharField(max_length=100)
    profile_image=models.ImageField(upload_to='myimage', blank=True)
    my_file=models.FileField(upload_to='doc', blank=True)
    