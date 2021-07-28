from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    color = models.CharField(max_length=30)
    number = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Comment(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
