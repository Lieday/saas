from django.db import models

# Create your models here.
class PageVisit(models.Model):
    # db -> table
    # id -> hidden -> primarykey -> autofield -> ,1,2,3,
    path = models.TextField(blank=True,null=True) #col
    timestemps = models.DateTimeField(auto_now_add=True) #col
