from django.db import models

class Banner(models.Model):
    description = models.TextField()
    timer = models.IntegerField()
    link = models.URLField()

    def __str__(self):
        return self.description
