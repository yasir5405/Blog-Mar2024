from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 122)
    name = models.CharField(max_length = 122)
    desciption = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name