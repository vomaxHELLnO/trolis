from django.db import models

class ListObject(models.Model):
    title = models.TextField()
    text = models.TextField()
