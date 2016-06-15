from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Data(models.Model):
    principle = models.DecimalField(default = 0, decimal_places = 2, max_digits = 10)
    rate = models.DecimalField(default = 0.05, decimal_places = 3, max_digits = 5)
    compoundings = models.IntegerField(default = 1)
    year = models.DecimalField(default = 0, decimal_places = 3, max_digits = 6)
    interest = models.DecimalField(default = 0, decimal_places = 2, max_digits = 10)
    total = models.DecimalField(default = 0, decimal_places = 2, max_digits = 10)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class Run(models.Model):
    description = models.CharField(max_length = 256)
    date = models.DateField(auto_now_add = True)
    data = models.ForeignKey(Data)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
