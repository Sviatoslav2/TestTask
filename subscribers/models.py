from django.db import models

# Create your models here.


class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=256)

    def __str__(self):
        return '%s - %s'% (self.name, self.email)


    class Meta:
        verbose_name = "buyer"
        verbose_name_plural = 'List of buyers'
