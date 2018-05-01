# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from datetime import *


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
		elif len(post_data["name"]) < 3:
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

		if len(post_data["date_hired"]) == 0:
			response["isValid"] = False
			response["errors"].append("Hired Date is required")
		# elif post_data["date_hired"] > date.today:
		# 	print str(date.today)
		# 	response["isValid"] = False
		# 	response["errors"].append("Must be a valid Date Hired")
		
		if response["isValid"]:
			response["user"] = User.objects.create(
				name = post_data["name"],
				username = post_data["username"].lower(),
				password = bcrypt.hashpw(post_data["password"].encode(), bcrypt.gensalt()),
				date_hired = post_data["date_hired"]
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
	password = models.CharField(max_length=255)
	date_hired = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()

class ItemManager(models.Manager):
	def Add_item(self, post_data):

		response = {
			"isValid": True,
			"errors": [],
			"user": None
			}
		if len(post_data["item_name"]) < 3:
			isValid = False
			response["errors"].append('Item name must be more than 3 characters')
		
		return response



class Item(models.Model):
    title=models.CharField(max_length=64)
    user=models.ForeignKey(User, related_name='items')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects = ItemManager()

class Wish(models.Model):
    wish=models.ForeignKey(Item, related_name='wishers')
    wisher=models.ForeignKey(User, related_name='wishes')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

