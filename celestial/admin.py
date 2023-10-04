from django.contrib import admin
from .models import Star, Planet, Moon, Resource

# Register your models here.
admin.site.register(Star)
admin.site.register(Planet)
admin.site.register(Moon)
admin.site.register(Resource)
