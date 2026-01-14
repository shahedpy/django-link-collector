from django.db import models


class ScrapedLink(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return self.name or self.address
