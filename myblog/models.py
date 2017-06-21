import uuid
from django.db import models
from datetime import datetime
from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.
class Story(models.Model):
	story_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True) 
	title = models.CharField(max_length=500)
	text = HTMLField()
	created_by = models.ForeignKey(User, editable=True)
	pub_date = models.DateTimeField(default=datetime.now,blank=True)


