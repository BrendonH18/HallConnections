from django.contrib import admin
from .models import *

class ActivityInLine(admin.TabularInline):
    model = Activity
    extra = 0
    min_num = 1

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [
        ActivityInLine
    ]
    pass
    # list_display = [
    #     "first_name",
    #     "last_name",
    # ]


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    pass