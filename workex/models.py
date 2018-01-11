# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.contrib.sitemaps import ping_google

# Create your models here.
class ExperienceDesc(models.Model):
	description = models.TextField()

	def __unicode__(self):
		return self.description

	def __str__(self):
		return self.description

class Experience(models.Model):
	company_name = models.CharField(max_length=250)
	location = models.CharField(max_length=250)
	listed_description = models.ManyToManyField('ExperienceDesc', blank=True, default="")
	from_date = models.DateField('FromDate')
	to_date = models.DateField('ToDate')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	slug = models.SlugField(unique=True, max_length=255)

	def __unicode__(self):
		return self.company_name

	def __str__(self):
		return self.company_name

	class Meta:
		ordering = ['-to_date']

	def get_absolute_url(self):
		return reverse('experience:experience_detail', kwargs={"experience_slug":self.slug})

	def save(self, *args, **kwargs):
		self.slug = slugify(self.company_name)
		try:
			ping_google()
		except Exception:
			pass
		return super(Experience, self).save(*args, **kwargs)





