# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.contrib.sitemaps import ping_google

# Create your models here.
class ProjectCategory(models.Model):
	title = models.CharField(max_length=150)
	slug = models.SlugField(unique=True, max_length=255)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		return super(ProjectCategory, self).save(*args, **kwargs)


class Project(models.Model):
	title = models.CharField(max_length=250)
	description = models.TextField()
	meta_description = models.TextField(null="", blank=True)
	category = models.ForeignKey('ProjectCategory', blank=True, null=True)
	featured_image = models.ImageField(upload_to='products/images/', null=True, blank=True)
	associated_images = models.ManyToManyField('ProjectImage',blank=True)
	date = models.DateField('Date')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	slug = models.SlugField(unique=True, max_length=255)
	ongoing = models.BooleanField(default=True)
	enable = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-date']

	def get_absolute_url(self):
		return reverse('project:project_detail', kwargs={"project_slug": self.slug})

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		try:
			ping_google()
		except Exception:
			pass
		return super(Project, self).save(*args, **kwargs)


class ProjectImage(models.Model):
	image = models.ImageField(upload_to='project/images/default.png')

	def __unicode__(self):
		return self.image.file.name