from django.shortcuts import render
from .models import Education, Course, Skill, Certificate, Experience, Project

def index(request):
    educations= Education.objects.all()
    courses=Course.objects.all()
    duras= Skill.objects.filter(type__contains = 'dura').order_by('order')
    blandas= Skill.objects.filter(type__contains = 'blanda').order_by('title')
    certificates= Certificate.objects.all()
    experiences= Experience.objects.all()
    projects= Project.objects.all()
    context={'educations':educations, 'courses':courses, 'duras':duras,
             'blandas':blandas, 'certificates':certificates, 'experiences':experiences, 'projects':projects}
    return render(request, 'index.html', context)