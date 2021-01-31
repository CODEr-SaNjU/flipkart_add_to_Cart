from django.db import models

class item_list(models.Model):
    item_name = models.CharField(max_length=200)
    item_brand = models.CharField(max_length = 200)
    item_image = models.ImageField(upload_to='media/',)
    item_size = models.CharField(max_length=10)
    item_price = models.CharField(max_length=10)

    def __str__(self):
        return self.item_name