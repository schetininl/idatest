from django.db import models
from django.core.validators import MinValueValidator


class Image(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to="img/", blank=False, null=False)
    width = models.IntegerField(blank=False, null=False, 
        validators=[MinValueValidator(1)])
    height = models.IntegerField(blank=False, null=False, 
        validators=[MinValueValidator(1)])

