# Register your models here.
from django.contrib import admin

from apps.userauths import models

admin.site.register(models.User)