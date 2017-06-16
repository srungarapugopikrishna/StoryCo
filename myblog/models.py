from django.db import models
from datetime import datetime
from tinymce.models import HTMLField
# Create your models here.
class Story(models.Model):

	title = models.CharField(max_length=500)
	text = HTMLField()
	pub_date = models.DateTimeField(default=datetime.now,blank=True)