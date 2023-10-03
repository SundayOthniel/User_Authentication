from django.db import models

class patientRecords(models.Model):
    surename = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    age = models.IntegerField()