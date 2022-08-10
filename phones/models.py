from django.db import models


class Phone(models.Model):
    id = models.PositiveIntegerField()
    name = models.CharField(max_length=250)
    price = models.PositiveIntegerField()
    image = models.URLField(max_length=200)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200, populate_from='name', unique=True, null=True)
