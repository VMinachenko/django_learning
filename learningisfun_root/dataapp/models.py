from django.db import models

# Create your models here.

class Packages(models.Model):
    package_name = models.CharField(max_length=100)
    stars = models.IntegerField()
    forks = models.IntegerField()

    class Meta:
        app_label = 'dataapp'