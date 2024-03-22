from django.db import models

class ScrapeResult(models.Model):
    ip = models.CharField(max_length=100)
    port = models.IntegerField()
    protocol = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    uptime = models.CharField(max_length=100)