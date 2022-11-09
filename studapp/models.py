from email.policy import default
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    phone = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def json(self):
        return {
            "stu_id": self.id,
            "name": self.name,
            "phone": self.phone,
            "created_date": self.created_date,
        }
    
    
    @property
    def formatted_date_created_date(self):
        return self.created_date.strftime("%d-%b-%y")


class StudentInfo(models.Model):
    stu_id = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="student", null=True, blank=True
    )
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def json(self):
        return {
            "state": self.state,
            "city": self.city,
        }

