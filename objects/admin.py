from django.contrib import admin

from .models import *


admin.site.register(OilField)
admin.site.register(Well)
admin.site.register(Layer)

admin.site.register(Lab)
admin.site.register(Object)
admin.site.register(LabObject)
admin.site.register(Task)


