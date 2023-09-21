from django.contrib import admin

from app.models import *


# Register your models here.
class Custom_Student(admin.ModelAdmin):
    list_display=['Sname','Sid','Semail']
    list_display_links=['Semail']
    list_editable=['Sid',]
    #list_display_links['sid'] here we cant perform both for one,----list_editable and list_display_links
    list_filter=['Sname']
    list_per_page=1
    admin.site.site_header='Model'
    admin.site.site_title='Student'
    admin.site.index_title='permissions'
admin.site.register(Student,Custom_Student)
