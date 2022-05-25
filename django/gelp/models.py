from django.db import models

class HomeValuess(models.Model):

    text = models.CharField(max_length=150)
    logo = models.CharField(max_length=60)

    def __str__(self):
        return self.logo

