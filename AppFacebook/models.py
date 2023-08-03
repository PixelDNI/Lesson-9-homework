from django.db import models

# Create your models here.


class User(models.Model):

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.BooleanField(verbose_name='Female')

    def __str__(self):
        return f'{self.name} - {self.surname} - {self.age}year old'

    def get_absolute_url(self):
        return f"/users/{self.id}"
