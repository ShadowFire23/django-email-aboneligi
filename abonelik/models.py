from django.db import models

class EmailAbonelik(models.Model):
    ad = models.CharField(max_length=70)
    soyad = models.CharField(max_length=70)
    email = models.EmailField()

    def __str__(self):
        return self.email