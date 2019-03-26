from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Blog(models.Model):
    caption = models.CharField(max_length=32)

    def __unicode__(self):
        return self.caption
