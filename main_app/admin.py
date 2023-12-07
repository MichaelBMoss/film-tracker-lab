from django.contrib import admin
from .models import Film, Director, Actor

# Register your models here.
admin.site.register(Film)
admin.site.register(Director)
admin.site.register(Actor)