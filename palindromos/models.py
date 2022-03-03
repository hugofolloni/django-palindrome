from django.db import models

# Create your models here.

class Palindromo(models.Model):
    palindromo = models.CharField(max_length=255)
    def __str__(self):
        return self.palindromo