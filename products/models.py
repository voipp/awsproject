from django.db import models


class Product(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    price = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')