from django.contrib import admin
from .models import Page, Event, Action, Release, Version


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_filter = ['location', 'released_at__release_status', 'released_at__release_version__version_str', 'target']


admin.site.register(Page)
admin.site.register(Event, EventAdmin)
admin.site.register(Action)
admin.site.register(Release)
admin.site.register(Version)
