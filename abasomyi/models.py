from django.db import models

class Umusomyi(models.Model):
    class Gender(models.TextChoices):
        GABO = 'M'
        GORE = 'F'
    email = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=130)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)
    sex = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=None
    )
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.sex}"