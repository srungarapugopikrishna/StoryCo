import uuid
from django.db import models
from datetime import datetime
from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.
class Genres(models.Model):
	genre_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
	genre_name = models.CharField(max_length=50)
# def __unicode__(self):
# 	return self.genre_name

class Story(models.Model):
	story_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
	#story_id = models.UUIDField(primary_key=True, editable=True)
	title = models.CharField(max_length=500)
	text = HTMLField()
	#genre_id = models.ForeignKey(Genres, default=uuid.uuid4)
	genre_id = models.ForeignKey(Genres, default=None)
	created_by = models.ForeignKey(User, editable=True)
	pub_date = models.DateTimeField(default=datetime.now,blank=True)
	# def __unicode__(self):
	# 	return str(self.title)

class relations(models.Model):
	relation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
	parent_id = models.CharField(max_length=500)
	child_id = models.CharField(max_length=500)
	# def __unicode__(self):
	# 	return str(self.relation_id)
