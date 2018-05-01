# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class user(models.Model):
	first_name = models.Charfield(max_length = 255)
	last_name = models.Charfield(max_length = 255)
	email = models.Charfield(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class books(models.Model):
	name = models.Charfield(max_length = 255)
	desc = models.Charfield(max_length = 1000)
	likes = models.ManyToManyField(user, related_name = 'liked')
	uploader = models.ForeignKey(user, related_name = 'uploaded_by')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at  = models.DateTimeField(auto_now = True)
	