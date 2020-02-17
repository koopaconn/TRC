from django.db import models

class model_name(models.Model):

    name = models.CharField(max_length=264,default="Name")

    def __str__(self):
        return self.name

class model_project(models.Model):

    projectDesc = models.CharField(max_length=264,default="Project")

    def __str__(self):
        return self.projectDesc

class model_utilization(models.Model):

    name = models.CharField(max_length=264)
    project = models.CharField(max_length=264)
    hours = models.FloatField(error_messages={'invalid':"Please enter hours or 0 to delete entry",'required':"Please enter hours or 0 to delete entry"})
    week = models.CharField(max_length=264)

    def __str__(self):
        return self.week+' '+self.name

    class Meta:
        ordering = ['name']
