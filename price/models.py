from django.db import models

# Create your models here.

class Developer(models.Model):
    name = models.CharField(max_length=50)
    job = models.CharField(max_length=100)
    img_path = models.CharField(max_length=255)

    git = models.CharField(max_length=255)
    tistory = models.CharField(max_length=255)
    notion = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Predict(models.Model):
    goo = models.CharField(max_length=50)
    dong = models.CharField(max_length=50)
    year = models.IntegerField()
    area = models.IntegerField()

    def __str__(self):
        return self.goo