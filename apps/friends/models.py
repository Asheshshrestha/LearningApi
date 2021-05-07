from django.db import models

# Create your models here.
class Friends(models.Model):
    f_name = models.TextField()
    l_name = models.TextField()
    number = models.TextField(null=True)
    email = models.EmailField()
    created_at = models.DateField(auto_now=True)
    