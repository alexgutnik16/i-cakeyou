from django.db import models


CATEGORIES = [('BC', 'Бисквитные торты'),
              ('MC', 'Муссовые торты'),
              ('DS', 'Дессерты'),
              ('MN', 'Мини торты')]


class Product(models.Model):
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=2, choices=CATEGORIES, default='BC', verbose_name="Категория")
    description = models.TextField(max_length=512)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Images(models.Model):
    name = models.CharField(max_length=64)
    photo = models.ImageField(upload_to='uploads/')
    default = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
