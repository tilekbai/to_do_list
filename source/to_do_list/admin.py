from django.contrib import admin
from to_do_list.models import Problem

# Register your models here.

class ProblemAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'dead_line']
    list_filter = ['description', 'status']
    search_fields = ['description', 'status']
    fields = ['description', 'status', 'dead_line']


admin.site.register(Problem, ProblemAdmin)
