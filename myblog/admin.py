from django.contrib import admin
from .models import Story,relations,Genres

# Register your models here.
admin.site.register(Story)
admin.site.register(relations)
admin.site.register(Genres)
