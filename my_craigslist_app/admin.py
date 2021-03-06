from django.contrib import admin

from .models import Search

# Register your models here.

admin.site.register (Search)            # the search table will be added in the DB and will show up in admin page
