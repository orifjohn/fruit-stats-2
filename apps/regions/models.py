from django.db import models
from django.db.models import Sum
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Region(MPTTModel):
    name = models.CharField(max_length=255, unique=True)
    position = models.PositiveBigIntegerField(default=1)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    @property
    def stock_count(self):
        return self.stocks.count()

    @property
    def fruit_tons(self):
        return self.stocks.aggregate(Sum("fruits__weight", default=0)).get("fruits__weight__sum")
