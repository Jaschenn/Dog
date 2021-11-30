from django.contrib import admin
from .models import Page, Event, Action, Release, Version, Media


class VersionFilter(admin.SimpleListFilter):
    title = '>= version'
    parameter_name = 'released_at'  # must is a field

    def lookups(self, request, model_admin):
        return (
            zip([v.version_str for v in Version.objects.all()], [v.version_str for v in Version.objects.all()])
        )

    def queryset(self, request, queryset):
        if self.value() == '1.9.73':
            print('选择了一个选项')
            return queryset.filter(released_at__release_version__version_str='1.9.73')
        else:
            return queryset


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_filter = ['location', 'released_at__release_status', 'released_at__release_version__version_str', 'target',
                   VersionFilter]
    list_display = ['action', 'location', 'target', 'extra', 'released_at']

    search_fields = ['location__page_name', 'extra']


admin.site.register(Page)
admin.site.register(Event, EventAdmin)
admin.site.register(Action)
admin.site.register(Release)
admin.site.register(Version)
admin.site.register(Media)
