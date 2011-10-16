from django.db import models


class Venues(models.Model):
    name = models.CharField(unique=True, max_length = 255)
    address = models.CharField(max_length = 255)
    latitude = models.FloatField(db_index=True)
    longitude = models.FloatField(db_index=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = u"venues"

class Sponsors(models.Model):
    name = models.CharField(unique=True, max_length = 255)
    venue = models.ForeignKey(Venues, null=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = u"sponsors"

class EventCategories(models.Model):
    name = models.CharField(unique=True, max_length = 255)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = u"event_categories"

class Events(models.Model):
    name = models.CharField(unique=True, max_length = 255)
    sponsor = models.ForeignKey(Sponsors)
    venue = models.ForeignKey(Venues)
    category = models.ForeignKey(EventCategories)
    start_time = models.DateTimeField()
    #TODO validate end time should be after start time
    end_time = models.DateTimeField()
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = u"events"

