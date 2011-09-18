from django.db import models
from django.contrib.sites.models import Site as Site_django

class Organization(models.Model):
    """
    Describing an Organization that uses geonition services
    """
    name = models.CharField(max_length=50,
                            primary_key=True)
    
class Site(models.Model):
    """
    An Organizations site and definitions of the site
    specific settings.
    """
    organization = models.ForeignKey(Organization)
    site = models.OneToOneField(Site_django)
    
    #site specific settings
    apps_in_use = models.ManyToManyField(Application)
    database = models.ForeignKey(Database)
    history = models.BooleanField()
    mongodb = models.BooleanField()
    
    class Meta:
        unique_together = (("organization", "site"),)

class Application(models.Model):
    """
    An application service provided by geonition
    """
    name = models.CharField(max_length=50,
                            primary_key=True)
    
    
class Database(models.Model):
    """
    Should support modification of the following fields:
    
    'ENGINE': 'django.contrib.gis.db.backends.postgis', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    'NAME': '',                      # Or path to database file if using sqlite3.
    'USER': '',                      # Not used with sqlite3.
    'PASSWORD': '',                  # Not used with sqlite3.
    'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
    'PORT': '',
    
    """
    
    name = models.CharField(max_length=30)
    host = models.IPAddressField()
    port = models.PositiveIntegerField()