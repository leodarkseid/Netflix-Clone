from distutils import core
from django.contrib import admin

from .models import Movies,Profile,CustomUser,Video

admin.site.register(Movies)
admin.site.register(Profile)
admin.site.register(CustomUser)
admin.site.register(Video)

# Register your models here.
