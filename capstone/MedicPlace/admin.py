from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Medic)
admin.site.register(Normal_User)
admin.site.register(Medic_Article)
admin.site.register(Article_comment)
admin.site.register(type_of_medicine)
admin.site.register(medicine)