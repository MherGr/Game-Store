from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return self.title
    
