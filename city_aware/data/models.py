from django.db import models

class RawAddresses(models.Model):
    longform = models.CharField(max_length=255)
    street = models.CharField(max_length=127)
    street_prefix = models.CharField(max_length=31, null=True)
    street_suffix = models.CharField(max_length=31, null=True)
    street_type = models.CharField(max_length=31, null=True)
    number = models.IntegerField()
    number_suffix = models.CharField(max_length=31, null=True)
    unit = models.CharField(max_length=63, null=True)
    municipality = models.CharField(max_length=255)
    county = models.CharField(max_length=127)
    state = models.CharField(max_length=63)
    zip_code = models.IntegerField()
    zip4 = models.IntegerField(null=True)
    latitude = models.FloatField(db_index=True)
    longitude = models.FloatField(db_index=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = u"raw_addresses"

class Municipalities(models.Model):
    name = models.CharField(max_length = 255)
    abbrev = models.CharField(max_length = 31)
    class Meta:
        db_table = u"municipalities"

class ZipCodes(models.Model):
    zip_code = models.IntegerField()
    class Meta:
        db_table = u"zip_codes"
        
class Counties(models.Model):
    name = models.CharField(max_length = 255)
    class Meta:
        db_table = u"counties"

class States(models.Model):
    name = models.CharField(max_length = 127)
    abbrev = models.CharField(max_length = 7)
    class Meta:
        db_table = u"states"

class Addresses(models.Model):
    longform = models.CharField(max_length=255)
    street = models.CharField(max_length=127)
    street_prefix = models.CharField(max_length=31, null=True)
    street_suffix = models.CharField(max_length=31, null=True)
    street_type = models.CharField(max_length=31, null=True)
    number = models.IntegerField()
    number_suffix = models.CharField(max_length=31, null=True)
    unit = models.CharField(max_length=63, null=True)
    municipality = models.ForeignKey(Municipalities)
    county = models.ForeignKey(Counties)
    state = models.ForeignKey(States)
    zip_code = models.ForeignKey(ZipCodes)
    zip4 = models.IntegerField(null=True)
    latitude = models.FloatField(db_index=True)
    longitude = models.FloatField(db_index=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = u"addresses"
