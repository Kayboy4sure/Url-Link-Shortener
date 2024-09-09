from django.db import models

# Create your models here.
class Urldata(models.Model):
    url = models.CharField(max_length=200)
    new_url = models.CharField(max_length=10)

    def __str__(self):
        return self.new_url +' '+ self.url