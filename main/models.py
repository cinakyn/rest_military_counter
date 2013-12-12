from django.db import models
from django.contrib import admin

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    accepted = models.BooleanField(default=False)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'end_date', 'accepted')
    ordering = ['accepted', 'id']
    actions = ['make_accepted', 'make_denied']
    
    def make_accepted(self, request, query_set):
        query_set.update(accepted=True)

    def make_denied(self, request, query_set):
        query_set.update(accepted=False)
    
    make_accepted.short_description = 'make accepted'
    make_denied.short_description = 'make denied'
