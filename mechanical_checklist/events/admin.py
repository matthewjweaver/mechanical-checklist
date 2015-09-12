from django.contrib import admin
from .models import Event, Incident

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    exclude = ["user"]
    readonly_fields = ["user"]
    list_display = [
        "event",
        "source",
	"timestamp",
	"description",
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(IncidentAdmin, self).save_model(request, obj, form, change)
