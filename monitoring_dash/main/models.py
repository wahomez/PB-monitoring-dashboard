from datetime import timezone
from django.db import models

# Create your models here.
class Test(models.Model):
    Date = models.DateField()
    Open = models.IntegerField()
    High = models.IntegerField()
    Close = models.IntegerField()

    def __str__(self):
        return self.Close