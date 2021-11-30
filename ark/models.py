from django.db import models


# Create your models here.
class Media(models.Model):
    media_name = models.CharField(max_length=200)
    media_content = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.media_name


class Page(models.Model):
    page_name = models.CharField(max_length=200)
    technology_stack_name = models.CharField(max_length=200)
    page_screenshot = models.ManyToManyField(Media, blank=True)

    def __str__(self):
        return self.page_name


class Action(models.Model):
    action_name = models.CharField(max_length=200)
    action_type = models.CharField(max_length=200)

    def __str__(self):
        return self.action_name


class Version(models.Model):
    version_str = models.CharField(max_length=200)
    version_code = models.IntegerField()

    def __str__(self):
        return '_'.join([self.version_str, str(self.version_code)])


class Event(models.Model):
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    location = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='triggered_on', null=True, blank=True)
    target = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='jumps_to', null=True, blank=True)
    extra = models.CharField(max_length=200)

    def __str__(self):
        return self.action.__str__() + self.target.__str__()


class Release(models.Model):
    release_datetime = models.DateTimeField()
    release_status = models.CharField(max_length=200)  # draft, pre-release, released
    release_version = models.ForeignKey(Version, on_delete=models.CASCADE, null=True, blank=True)
    release_pages = models.ManyToManyField(Page, blank=True, related_name='release_pages')
    release_events = models.ManyToManyField(Event, blank=True, related_name='release_events')

    def __str__(self):
        return self.release_status + '_' + self.release_datetime.strftime('%m/%d/%Y_%H:%M:%S')


