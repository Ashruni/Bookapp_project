from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import datetime
class regmodel(models.Model):
    username = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20)



# class uploadmodel1(models.Model):
#     bookname =models.CharField(max_length=30)
#     bookpdf =models.FileField(upload_to='bookmsapp/static')
#     author =models.CharField(max_length=40)
#     # bookdate =models.DateTimeField(default=str(datetime.date.today()))
#     bookdate = models.DateTimeField(auto_now_add=True)
#     image =models.FileField(upload_to='bookmsapp/static')
#     def __str__(self):
#         return self.bookname
class uploaddisplaym(models.Model):
    bookname =models.CharField(max_length=40)
    bookpdf =models.FileField(upload_to='bookmsapp/static')
    uploaddate =models.DateField(auto_now_add=True)
    bookimage =models.FileField(upload_to='bookmsapp/static')
    bookauthor =models.CharField(max_length=30)
