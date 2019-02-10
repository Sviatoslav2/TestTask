from django.db import models
from django.db.models.signals import post_save

# Create your models here.


class Car(models.Model):
    brand_TYPES = (
        ('volkswagen', 'Volkswagen'),
        ('mitsubishi', 'Mitsubishi'),
        ('ford', 'Ford '),
        ('lamborghini', 'Lamborghini'),
    )

    model_TYPES = (
        ('model1', 'Model1'),
        ('model2', 'Model2'),
        ('model3', 'Model3'),
        ('model4', 'Model4'),
    )

    brand = models.CharField(max_length=256, choices=brand_TYPES)
    model = models.CharField(max_length=256, choices=model_TYPES)
    year = models.IntegerField()
    price = models.IntegerField()
    nameOfOvner = models.CharField(max_length=256)
    #published_date = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=16, blank=True, default='')


    def __str__(self):
        #return "%s - %s" % (self.word, self.definition)
        return 'The brand is %s( %s ),  the category is - %s , it will be cost %s. The owner name is %s.'% (self.brand, self.model, self.category, self.price,self.nameOfOvner)


def get_category(**kwargs):
    instance = kwargs.get('instance')

    if instance.category == '':
        if instance.year < 1990:
            instance.category = '1990-'
        elif 1990 <= instance.year < 2000:
            instance.category = '1990-2000'
        elif 2000 <= instance.year < 2010:
            instance.category = '2000-2010'
        elif instance.year > 2010:
            instance.category = '2010+'

        instance.save()

post_save.connect(get_category, Car)
