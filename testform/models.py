from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings

class model_testform(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="author", null=True, blank=True, on_delete=models.SET_NULL)
    editBy = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="editBy", null=True, blank=True, on_delete=models.SET_NULL)
    parkSpecialLane = models.CharField(max_length=264)
    blockID = models.CharField(max_length=264,unique=True,error_messages={'unique':"This Block ID already exists."})
    consistantBlock = models.CharField(max_length=264)
    rodwayType = models.CharField(max_length=264)
    medianType = models.CharField(max_length=264)
    horAlignment = models.CharField(max_length=264)
    speedLimit = models.CharField(max_length=264)
    shoulderTypeDec = models.CharField(max_length=264)
    shoulderWidthDec = models.BigIntegerField(null=True,blank=True)
    gutterWidthDec = models.BigIntegerField(null=True,blank=True)
    rightLWidthDec = models.BigIntegerField(null=True,blank=True)
    centerLWidthDec = models.BigIntegerField(null=True,blank=True)
    LeftLWidthDec = models.BigIntegerField(null=True,blank=True)
    shoulderTypeInc = models.CharField(max_length=264)
    shoulderWidthInc = models.BigIntegerField(null=True,blank=True)
    gutterWidthInc = models.BigIntegerField(null=True,blank=True)
    rightLWidthInc = models.BigIntegerField(null=True,blank=True)
    centerLWidthInc = models.BigIntegerField(null=True,blank=True)
    LeftLWidthInc = models.BigIntegerField(null=True,blank=True)
    comment = models.CharField(max_length=264)
    state = models.CharField(max_length=264)

    def __str__(self):
        return self.blockID

    def get_absolute_url(self):
        return reverse('testform:view_testformUpdate', args=[str(self.pk)])

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
