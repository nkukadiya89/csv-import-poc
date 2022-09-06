from django.db import models
from django.conf import settings


class Product(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="product",
        null=True,
    )
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50, null=False, blank=False)
