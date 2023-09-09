from django.db import models


class Stock(models.Model):
    region = models.ForeignKey("regions.Region", on_delete=models.CASCADE, related_name="stocks")
    name = models.CharField(max_length=255)


class Fruit(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="fruits")
    name = models.CharField(max_length=255)
    weight = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
