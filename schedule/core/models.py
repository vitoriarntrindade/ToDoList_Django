from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, timedelta


class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_date_input_event(self):
        return self.event_date.strftime('%Y-%m-%dT%H:%M')

    def get_event_late(self):
        return self.event_date < datetime.now()

    def get_event_less_than_1h_left(self):
        return self.event_date - timedelta(hours=1) < datetime.now() < self.event_date
