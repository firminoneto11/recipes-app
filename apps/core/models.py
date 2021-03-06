from django.db import models


class Recipe(models.Model):
    class Meta:
        db_table = "recipes"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    key = models.TextField()
