from django.db import models

# Create your models here.
class Story(models.Model):
    title        = models.CharField(max_length=100, blank=False)
    token        = models.CharField(max_length=100, blank=False)
    lastEditTime = models.DateTimeField(auto_now_add=True)
    liked        = models.IntegerField()
    generateFlightTimes    = models.IntegerField()

    class Meta:
        unique_together = ('title','token','lastEditTime')
        ordering = ('lastEditTime','title',)

class Customer(models.Model):
    story = models.ForeignKey(Story, related_name='customers')
    registeredTime = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, blank=False)
    pwd  = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=254, blank=True)
    token = models.CharField(max_length=100, blank=False)
    class Meta:
        # unique_together = ('username','email')
        ordering = ('username',)

class Place(models.Model):
    story = models.ForeignKey(Story, related_name='places')
    placeName = models.CharField(max_length=100, blank=False)
    timeVisited= models.DateTimeField(auto_now_add=False)
    timeLeft   = models.DateTimeField(auto_now_add=False)
    class Meta:
        # unique_together = ('placeName')
        ordering = ('placeName',)
