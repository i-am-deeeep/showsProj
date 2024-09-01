from django.db import models

# Create your models here.

class Shows(models.Model):
    name=models.CharField(max_length=30)
    date=models.DateField()
    rating=models.IntegerField()
    fav_character=models.CharField(max_length=20)

    def __str__(self):
        return self.name

