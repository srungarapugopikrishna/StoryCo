from django.contrib import admin
from .models import Story,Relations,Genres,Category,Episode,Relationship,Item,RepresentationType,ContentType

# Register your models here.
admin.site.register(Story)
admin.site.register(Relations)
admin.site.register(Genres)
admin.site.register(Category)
admin.site.register(Episode)
admin.site.register(Relationship)
admin.site.register(Item)
admin.site.register(ContentType)
admin.site.register(RepresentationType)