from django.contrib import admin

from catalog.models import Books, Orders

admin.site.register(Books)
admin.site.register(Orders)