from django.db import models
from django.contrib import admin

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    accepted = models.BooleanField(default=False)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('accepted', 'name', 'start_date', 'end_date')
