# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from datetime import *

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

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

		if len(post_data["alias"]) < 1:
			response["isValid"] = False
			response["errors"].append("Alias name is required")
		elif len(post_data["alias"]) < 3:
			response["isValid"] = False
			response["errors"].append("Alias name must be 3 characters or longer")

		if len(post_data["email"]) < 1:
			response["isValid"] = False
			response["errors"].append("Email is required")
		elif not EMAIL_REGEX.match(post_data["email"]):
			response["isValid"] = False
			response["errors"].append("Invalid email")
		else:
			list_of_users_matching_email = User.objects.filter(email=post_data["email"].lower())
			if len(list_of_users_matching_email) > 0:
				response["isValid"] = False
				response["errors"].append("Email is already in use")

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

		if len(post_data["dob"]) == 0:
			response["isValid"] = False
			response["errors"].append("Date of Birth is required")
		elif post_data["dob"] >= date.today:
			response["isValid"] = False
			response["errors"].append("You can not born now or in the future")
		
		if response["isValid"]:
			response["user"] = User.objects.create(
				name = post_data["name"],
				alias = post_data["alias"],
				email = post_data["email"].lower(),
				password = bcrypt.hashpw(post_data["password"].encode(), bcrypt.gensalt()),
				birthday = post_data["dob"]
			)

		return response

	def login(self, post_data):
		
		response = {
			"isValid": True,
			"errors": [],
			"user": None
		}

		if len(post_data["email"]) < 1:
			response["isValid"] = False
			response["errors"].append("Email is required")
		elif not EMAIL_REGEX.match(post_data["email"]):
			response["isValid"] = False
			response["errors"].append("Invalid email")
		else:
			list_of_users_matching_email = User.objects.filter(email=post_data["email"].lower())
			if len(list_of_users_matching_email) < 1:
				response["isValid"] = False
				response["errors"].append("Unknown email {}".format(post_data["email"]))

		if len(post_data["password"]) < 1:
			response["isValid"] = False
			response["errors"].append("Password is required")
		elif len(post_data["password"]) < 8:
			response["isValid"] = False
			response["errors"].append("Password must be 8 characters or longer")

		if response["isValid"]:
			user = list_of_users_matching_email[0]
			if not bcrypt.checkpw(post_data["password"].encode(), user.password.encode()):
				response["isValid"] = False
				response["errors"].append("Incorrect password")
			else:
				response["user"] = user
			
		return response

class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	birthday = models.DateTimeField()
	favorites = models.ManyToManyField("Quote", related_name="favorites", default=None)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()


class QuoteManager(models.Manager):
	def validateQuote(self, post_data):

		response = {
			"isValid": True,
			"errors": [],
			"user": None
		}

		
		if len(post_data["content"]) < 10:
			isValid = False
			response["errors"].append('Message must be more than 10 characters')
		return response

class Quote(models.Model):
	content = models.CharField(max_length = 255)
	author = models.CharField(max_length = 255)
	poster = models.ForeignKey(User, related_name = 'authored_quotes')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = QuoteManager()

	def __str__(self):
		return 'content:{}, author:{}'.format(self.content, self.user)

