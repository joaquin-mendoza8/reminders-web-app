from django.db import models

class Reminder(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due = models.DateTimeField()
