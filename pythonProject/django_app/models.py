from django.db import models


class Todos(models.Model):
    title = models.CharField(max_length=128)
    desc = models.TextField()

    def __str__(self):
        return str(f"{self.title}")

    def __repr__(self):
        return str(f"{self.title}")
