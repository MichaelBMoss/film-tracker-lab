from django.contrib import admin
from .models import Film, Screening, Actor

admin.site.register(Film)
admin.site.register(Screening)
admin.site.register(Actor)