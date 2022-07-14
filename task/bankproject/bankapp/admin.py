from django.contrib import admin

# Register your models here.

from bankapp.models import branch, userdetail,place

admin.site.register(branch)
admin.site.register(userdetail)
admin.site.register(place)
