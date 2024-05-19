from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "event_date", "created_at")
    list_filter = ("title",)


admin.site.register(Event, EventAdmin)
