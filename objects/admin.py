from django.contrib import admin

from .models import *

class LabObjectAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'author',
    )


admin.site.register(OilField)
admin.site.register(Well)
admin.site.register(Layer)

admin.site.register(Lab)
admin.site.register(Object)
admin.site.register(LabObject, LabObjectAdmin)
admin.site.register(Task)


