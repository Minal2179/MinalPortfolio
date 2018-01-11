# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Experience, ExperienceDesc
# Register your models here.

class ExperienceAdmin(admin.ModelAdmin):
	list_display = ("company_name", "location", "from_date", "to_date")

admin.site.register(Experience, ExperienceAdmin)
admin.site.register(ExperienceDesc)