import imp
from django.contrib import admin
from .models import Project, Message
# Register your models here.

admin.site.register(Project)
admin.site.register(Message)
