from django.contrib import admin
from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'fullname',
        'bio',
        'lesson_price',
        'language',
    )
    list_display_links = (
        'fullname',
    )
    list_filter = (
        'lesson_price',
        'language',
    )
    search_fields = (
        'fullname',
        'lesson_price',
        'language',
    )
    prepopulated_fields = {'url': ('fullname', )}


admin.site.register(Teacher, TeacherAdmin)
