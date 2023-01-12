from django.contrib import admin
from .models import Education, Certificate, Skill, Experience, Project, Course
"""
class EducationAdmin(admin.ModelAdmin):

    list_display= ('name', 'title', 'start_date', 'end_date')
"""
admin.site.register(Education)
admin.site.register(Certificate)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Course)
