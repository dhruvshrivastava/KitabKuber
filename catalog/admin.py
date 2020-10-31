from django.contrib import admin

from catalog.models import Books, Orders, Sell

admin.site.register(Books)
admin.site.register(Orders)
admin.site.register(Sell)
