from django.db import models


class Category(models.Model):
    name = models.CharField('name', max_length=50)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'


class Product(models.Model):
    name = models.CharField('name', max_length=50)
    price = models.FloatField('price')
    description = models.TextField('description')
    count = models.IntegerField('count')
    is_active = models.BooleanField('status')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'is_active': self.is_active,
        }

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'




