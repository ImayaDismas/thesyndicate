from django.contrib import admin

# Register your models here.
from posts.models import Question

admin.site.register(Question)