# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from django.contrib.sitemaps import ping_google

# Create your models here.
class Skill(models.Model):
	title = models.CharField(max_length=250)
	percentage = models.PositiveIntegerField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	slug = models.SlugField(unique=True, max_length=255)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		try:
			ping_google()
		except Exception:
			pass
		return super(Skill, self).save(*args, **kwargs)
