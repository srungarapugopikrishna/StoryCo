from django.contrib import admin
from .models import Story,relations,Genres,Category,Episode,Relationship,Item

# Register your models here.
admin.site.register(Story)
admin.site.register(relations)
admin.site.register(Genres)
admin.site.register(Category)
admin.site.register(Episode)
admin.site.register(Relationship)
admin.site.register(Item)

