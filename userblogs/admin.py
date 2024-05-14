from django.contrib import admin
from userblogs.models import Userblog
# Register your models here.


class UblogAdmin(admin.ModelAdmin):
    list_display=['bname','buid','bcat','btitle','bimages','bdate','bshort_description','bdescription']
    list_filter=['buid','bcat','bdate']

admin.site.register(Userblog,UblogAdmin)