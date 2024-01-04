from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(Department)

admin.site.register(Employee)

admin.site.register(Salgrade)

admin.site.register(Bonus)