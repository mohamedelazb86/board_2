from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


from .models import Job,Category,Location,ApplyUser

class JobAdmin(SummernoteModelAdmin):
    list_display=['title','job_type','salary']
    search_fields=['title','descriptions']
    list_filter=['category']
    summernote_fields=('descriptions')

admin.site.register(Job,JobAdmin)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(ApplyUser)
