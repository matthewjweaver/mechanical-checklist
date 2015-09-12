from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Incident(models.Model):
    SOURCE_NIST_RSS, SOURCE_MANUAL = range(2)

    description = models.TextField()
    event = models.ForeignKey(Event)
    source = models.IntegerField(choices=[
        (SOURCE_NIST_RSS, "NIST CVE RSS"),
	(SOURCE_MANUAL, "Manual"),
    ])
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User)

class Subscription(models.Model):
    event = models.ForeignKey(Event)
    timestamp = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User)

    def get_absolute_url(self):
        return "/subscriptions/view/{self.id}/".format(self=self)

class NotificationChannel(models.Model):
    KIND_EMAIL, = range(1)

    subscription = models.ForeignKey(Subscription)
    kind = models.IntegerField(choices=[
        (KIND_EMAIL, "Email"),
    ])

class ChecklistItem(models.Model):
    subscription = models.ForeignKey(Subscription)
    text = models.TextField()
    timestamp = models.DateTimeField()

class IncidentChecklistItem(models.Model):
    incident = models.ForeignKey(Incident)
    checklist_item = models.ForeignKey(ChecklistItem)
    completed = models.BooleanField()

