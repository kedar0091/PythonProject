from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

    # def json(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #     }
