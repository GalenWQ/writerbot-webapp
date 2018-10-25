from django.db import models

class Story(models.Model):
    sentences = models.TextField()


