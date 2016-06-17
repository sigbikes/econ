from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Data(models.Model):
    name = models.CharField(max_length = 128, default = 'Blank')
    principle = models.DecimalField(default = 0, decimal_places = 2, max_digits = 10)
    rate = models.DecimalField(default = 0.05, decimal_places = 3, max_digits = 5)
    compoundings = models.IntegerField(default = 1)
    year = models.DecimalField(default = 0, decimal_places = 3, max_digits = 6)
    interest = models.DecimalField(default = 0, decimal_places = 2, max_digits = 10)
    total = models.DecimalField(default = 0, decimal_places = 2, max_digits = 10)


    class Meta:
        verbose_name_plural = "Data"

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class Run(models.Model):
    name = models.CharField(max_length = 128, default = 'Blank')
    description = models.CharField(max_length = 256, null = True)
    date = models.DateField(auto_now_add = True)
    data = models.ForeignKey(Data)

    def __str__(self):
        return self.description
    def __unicode__(self):
        return self.description
