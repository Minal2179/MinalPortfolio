# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Project, ProjectCategory, ProjectImage

class ProjectAdmin(admin.ModelAdmin):
	list_display = ("title", "category", "date", "ongoing", "enable")
# Register your models here.

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory)
admin.site.register(ProjectImage)
