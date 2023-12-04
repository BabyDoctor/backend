from django.contrib import admin
from .models import Test,Disease,Schedule

# Register your models here.
admin.site.register(Test)
admin.site.register(Disease)
admin.site.register(Schedule)