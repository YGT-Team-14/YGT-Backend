from django.contrib import admin
from .models import Friend_Post, Mento_Post,Profile,Mento_Comment

admin.site.register(Mento_Post)
admin.site.register(Friend_Post)
admin.site.register(Profile)
admin.site.register(Mento_Comment)