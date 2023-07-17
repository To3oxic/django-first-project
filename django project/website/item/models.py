from django.db import models
from django.contrib.auth.models import User

class Catagory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Catagories'

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Catagory, on_delete=models.CASCADE, related_name='items')
    image=models.ImageField(upload_to='item_images/',blank=True,null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name