# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Skill
# Register your models here.

class SkillAdmin(admin.ModelAdmin):
	list_display = ("title", "percentage")

admin.site.register(Skill, SkillAdmin)