from django.contrib import admin
from .models import Course, PaymentPage, Module
from embed_video.admin import AdminVideoMixin


# Register your models here.

class ModuleInline(admin.StackedInline):
    model = Module


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published',)
    list_display_links = ('id', 'name',)
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_par_page = 25
    inlines = [ModuleInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(PaymentPage)
