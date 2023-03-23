from django.db import models



class Phone(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    image = models.URLField(default='')
    release_date = models.DateField(default=1)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200)




