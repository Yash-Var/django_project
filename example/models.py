
from django.db import models


class Like(models.Model):
   count= models.IntegerField()
   


class Dislike(models.Model):
   temp= models.IntegerField()
   