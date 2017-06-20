from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
   title=models.CharField(max_length=120)
   content=models.TextField(null=True)
   create_time=models.DateTimeField(auto_now=True)
   modify_time=models.DateTimeField(auto_now_add=True,null=True)

   def __unicode__(self):
      return self.title