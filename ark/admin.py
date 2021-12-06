from django.contrib import admin
from .models import Page, Event, Action, Release, Version, Media, ReservedWord


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
            return queryset  # queryset.filter(released_at__release_version__version_str='1.9.73')
        else:
            return queryset


# Register your models here.
class EventInline(admin.TabularInline):
    model = Release.release_events.through


class EventAdmin(admin.ModelAdmin):
    list_filter = ['location', 'target', VersionFilter]
    list_display_links = []
    list_display = [
        'action',
        'location',
        'target',
        'extra',
    ]
    search_fields = ['location__page_name', 'extra']
    fk_fields = ['location_id']
    inlines = [EventInline, ]
    # autocomplete_fields = ['action', 'location', 'target']
    list_editable = ['extra', 'location']
    list_per_page = 20


class ReleaseAdmin(admin.ModelAdmin):
    list_display = ['release_datetime', 'release_status', 'affected_pages']
    filter_horizontal = ['release_pages', 'release_events']

    def affected_pages(self, obj):
        return [i.page_name for i in obj.release_pages.all()]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "release_events":
            kwargs["queryset"] = Event.objects.filter(release_events__release_status='draft')
        return super(ReleaseAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Page)
admin.site.register(Event, EventAdmin)
admin.site.register(Action)
admin.site.register(Release, ReleaseAdmin)
admin.site.register(Version)
admin.site.register(Media)
admin.site.register(ReservedWord)

