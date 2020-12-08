import uuid
from django.db import models
from django.urls import reverse


class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:items_by_category', args=[self.id])

    def __str__(self):
        return self.name



class Item(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length = 200)
    brand = models.CharField(max_length = 200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price =  models.DecimalField(max_digits = 6, decimal_places = 2)
    cover = models.ImageField(upload_to='covers/', blank=True)
    stock = models.IntegerField(null=True)
    avaliable = models.BooleanField(default=True, null=True)
    
    class Meta:
        ordering = ('title',)
        verbose_name = 'item'
        verbose_name_plural = 'items'

    def get_absolute_url(self):
        return reverse('shop:item_detail', args=[self.category.id, self.id])

    def __str__(self):
        return self.title


