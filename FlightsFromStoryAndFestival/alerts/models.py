from django.db import models

# Create your models here.

class UserAlert(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, blank=False)
    token = models.CharField(max_length=100, blank=False)
    alert_name = models.CharField(max_length=100, blank=False)
    ALERT_SEVERITY_CHOICES = (
        ('S1', 'CRITICAL'), 
        ('S2', 'MAJOR'),
        ('S3', 'MODERATE'),
        ('S4', 'MINOR'),
        ('S5', 'INFORMATION'),
    )
    alert_severity = models.CharField(max_length=2,
                                      choices=ALERT_SEVERITY_CHOICES,
                                     default='S1')
    alert_expression = models.CharField(max_length=50, blank=False)
    ALERT_CHOICES = (
        ('active','ACTIVE'),
        ('disabled','DISABLED')
    )
    status = models.CharField(max_length=10,choices=ALERT_CHOICES,default='active')
    last_triggered = models.FloatField(default=0)
    frequency = models.FloatField(default=60)
    class Meta:
        unique_together = ('alert_name', 'username', 'token')
        ordering = ('created',)

class AlertAction(models.Model):
    alert = models.ForeignKey(UserAlert, related_name='actions')
    ACTION_CHOICES = (
        ('email', 'EMAIL'), 
        ('api', 'API'),
        ('sms', 'SMS'),
        ('slack', 'SLACK'),
        ('pager', 'PAGER'),
    )
    alert_choice = models.CharField(max_length=5,
                                    choices=ACTION_CHOICES,
                                    default='email')
    action_email = models.EmailField(max_length=254, blank=True)
    action_api_url = models.URLField(max_length=200, blank=True)
    action_payload = models.TextField(blank=True)
    class Meta:
        ordering = ('alert',)

class AlertRule(models.Model):
    alert = models.ForeignKey(UserAlert, related_name='rules')
    STATS_FUNCTION_CHOICES = (
        ('avg', 'AVERAGE'),
        ('max', 'MAXIMUM'),
        ('min', 'MINIMUM'),
        ('val', 'VALUE'),
    )
    stats_function_operator = models.CharField(max_length=3,
                                               choices=STATS_FUNCTION_CHOICES,
                                               default='val')
    rule_name = models.CharField(max_length=100, blank=False)
    metric_key = models.CharField(max_length=100, blank=False)
    metric_name = models.CharField(max_length=100, blank=False)
    metric_threshold = models.CharField(max_length=100, blank=False)
    metric_evaluator = models.CharField(max_length=100, blank=False)
    metric_timeperiod = models.CharField(max_length=100, blank=True, default='')
    class Meta:
        unique_together = ('alert', 'rule_name', 'metric_name', 'metric_key')
        ordering = ('alert',)

##################################################################
##################################################################

class Story(models.Model):
    title        = models.CharField(max_length=100, blank=False)
    lastEditTime = models.DateTimeField(auto_now_add=True)
    liked        = models.IntegerField()
    generated    = models.IntegerField()
    class Meta:
        unique_together = ('title','lastEditTime')
        ordering = ('lastEditTime','title',)

class Customer(models.Model):
    story = models.ForeignKey(Story, related_name='customer')
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


