from django.contrib import admin
from .models import Report, Comment, NewUser

# Register your models here.
admin.site.register(Comment)
admin.site.register(Report)
admin.site.register(NewUser)

