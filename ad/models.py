from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Advertisement(models.Model):

    STATUS_CHOICES = (
        (1, "ACTIVE"),
        (2, "RESOLVED"),
        (3, "SOLD"),
    )

    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ads")
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=19)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

