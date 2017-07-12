import uuid
from django.db import models
from datetime import datetime
from tinymce.models import HTMLField
from django.core.validators import URLValidator
from django.contrib.auth.models import User

class Genres(models.Model):
	genre_id 	= 	models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
	genre_name 	= 	models.CharField(max_length=50)
# def __unicode__(self):
# 	return self.genre_name

class Story(models.Model):
	story_id 	= 	models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
	title 		= 	models.CharField(max_length=500)
	text 		= 	HTMLField()
	genre_id 	= 	models.ForeignKey(Genres, default=None)
	created_by 	= 	models.ForeignKey(User, editable=True)
	pub_date 	= 	models.DateTimeField(default=datetime.now,blank=True)
	# def __unicode__(self):
	# 	return str(self.title)

class relations(models.Model):
	relation_id = 	models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
	parent_id 	= 	models.CharField(max_length=500)
	child_id 	= 	models.CharField(max_length=500)
	# def __unicode__(self):
	# 	return str(self.relation_id)



class Category(models.Model):
	category_id 			= 	models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
	category_label 			= 	models.CharField(max_length=50)
	category_description 	= 	models.CharField(max_length=500)

class Content_Type(models.Model):
	content_id 		= 	models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
	content_type 	= 	models.CharField(max_length=20)

# It specifies the wether the category is story or poem or picture
class Representation_Type(models.Model):
	representation_id 	= 	models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
	representation_type = 	models.CharField(max_length=20)

class Item(models.Model):
	item_id 			= 	models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
	item_type 			= 	models.ForeignKey(Representation_Type,default=None)
	item_title 			=	models.CharField(max_length=500)
	item_description	=	models.CharField(max_length=1000)
	created_by			=	models.ForeignKey(User, editable=True)
	pub_date			=	models.DateTimeField(default=datetime.now,blank=True)


class Episode(models.Model):
	episode_id 						= 	models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
	episode_type 					= 	models.ForeignKey(Representation_Type,default=None)
	episode_description 			= 	models.CharField(max_length=500)
	episode_content_type 			= 	models.ForeignKey(Content_Type,default=None)
	episode_content 				=	HTMLField()
	episode_content_relative_url 	=   models.TextField(validators=[URLValidator()])
	categories 						=   models.CharField(max_length=500)
	created_by						=	models.ForeignKey(User, editable=True)
	pub_date						=	models.DateTimeField(default=datetime.now,blank=True)

class Relationship(models.Model):
	relation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
	parent_id = models.CharField(max_length=500)
	child_id = models.CharField(max_length=500)