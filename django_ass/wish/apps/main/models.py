# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from datetime import datetime

class UserManager(models.Manager):
	def register(self, post_data):
		
		response = {
			"isValid": True,
			"errors": [],
			"user": None
		}

		if len(post_data["name"]) < 1:
			response["isValid"] = False
			response["errors"].append("Name is required")
		elif len(post_data["name"]) < 3:
			response["isValid"] = False
			response["errors"].append("Name must be 3 characters or longer")

		if len(post_data["username"]) < 1:
			response["isValid"] = False
			response["errors"].append("Username is required")
		elif len(post_data["username"]) < 3:
			response["isValid"] = False
			response["errors"].append("Username must be 3 characters or longer")

		if len(post_data["password"]) < 1:
			response["isValid"] = False
			response["errors"].append("Password is required")
		elif len(post_data["password"]) < 8:
			response["isValid"] = False
			response["errors"].append("Password must be 8 characters or longer")

		if len(post_data["pass_conf"]) < 1:
			response["isValid"] = False
			response["errors"].append("Confim Password is required")
		elif post_data["pass_conf"] != post_data["password"]:
			response["isValid"] = False
			response["errors"].append("Confirm Password!!!")

		if len(post_data["date"]) == 0:
			response["isValid"] = False
			response["errors"].append("date hired is required")
		elif post_data['date'] >= datetime.now:
			response["isValid"] = False
			response["errors"].append("enter valid date hired")
		
		if response["isValid"]:
			response["user"] = User.objects.create(
				name = post_data["name"],
				username = post_data["username"].lower(),
				password = bcrypt.hashpw(post_data["password"].encode(), bcrypt.gensalt()),
				date_hired = post_data["date"]
			)

		return response

	def login(self, post_data):
		
		response = {
			"isValid": True,
			"errors": [],
			"user": None
		}

		if len(post_data["username"]) < 1:
			response["isValid"] = False
			response["errors"].append("Username is required")
		else:
			list_of_users_matching_username = User.objects.filter(username=post_data["username"].lower())
			if len(list_of_users_matching_username) < 1:
				response["isValid"] = False
				response["errors"].append("Unknown username {}".format(post_data["username"]))

		if len(post_data["password"]) < 1:
			response["isValid"] = False
			response["errors"].append("Password is required")
		elif len(post_data["password"]) < 8:
			response["isValid"] = False
			response["errors"].append("Password must be 8 characters or longer")

		if response["isValid"]:
			user = list_of_users_matching_username[0]
			if not bcrypt.checkpw(post_data["password"].encode(), user.password.encode()):
				response["isValid"] = False
				response["errors"].append("Incorrect password")
			else:
				response["user"] = user
			
		return response

class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	date_hired = models.DateTimeField()
	wishes = models.ManyToManyField("Items", related_name="favorites", default=None)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()


class ItemsManager(models.Manager):
	def Validate(self, item_name):

		response = {
			"isValid": True,
			"errors": [],
			"user": None
		}

		if len(item_name) < 3:
			isValid = False
			response["errors"].append('Message must be more than 3 characters')
		return response

class Items(models.Model):
	item_name = models.CharField(max_length = 255)
	poster = models.ForeignKey(User, related_name = 'poster')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = ItemsManager()

	def __str__(self):
		return 'item_name:{}'.format(self.item_name)

