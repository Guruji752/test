from django.contrib import admin
from .models import Writing,HealthCare_VideoLesson,HomeCare,HealthCare_LiveSession,HealthCare_OnlineConseltant,Research,Translation

# Register your models here.
admin.site.register(Writing)
admin.site.register(HealthCare_VideoLesson)
admin.site.register(HomeCare)
admin.site.register(Research)
admin.site.register(Translation)
admin.site.register(HealthCare_LiveSession)
admin.site.register(HealthCare_OnlineConseltant)
