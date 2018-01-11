# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import AboutMe
from project.models import Project
from workex.models import Experience
from workex.models import ExperienceDesc
from skill.models import Skill

# Create your views here
def home(request): #http request
	aboutme = AboutMe.objects.all()[:1]
	project_list = Project.objects.all().filter(enable=True)
	experience_list = Experience.objects.all()
	experience_desc = ExperienceDesc.objects.all() 
	skill = Skill.objects.all()
	template = "index.html"
	context = {
		"site_title": "Minal Shettigar Website",
		"aboutme": aboutme,
		"project_list": project_list,
		"experience_list": experience_list,
		"experience_desc": experience_desc,
		"skill": skill,
	}
	return render(request, template, context)

	