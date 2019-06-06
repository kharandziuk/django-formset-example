from django.db import models
from django.urls import reverse

class Owner(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


class Aggregate(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
