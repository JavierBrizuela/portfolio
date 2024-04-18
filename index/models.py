from django.db import models

# Create your models here.
class Education(models.Model):
    
    name= models.CharField(max_length=50, null=False, blank=False)
    title= models.CharField(max_length=100, null=False, blank=False)
    start_date= models.DateField(null=False, blank=False)
    end_date= models.DateField()

    def __str__(self) -> str:
        return self.name

class Certificate(models.Model):

    headline= models.CharField(max_length=50, null=False, blank=False)
    file_name= models.ImageField(upload_to="certificate", null=True, blank=True)
    visibility= models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.headline

class Skill(models.Model):
    
    type= models.CharField(max_length=20, null=False, blank=False)
    title= models.CharField(max_length=50, null=False, blank=False)
    image= models.ImageField(upload_to="skill", blank=True, null=True)
    order= models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title

class Experience(models.Model):

    company= models.CharField(max_length=50, null=False, blank=False)
    job= models.CharField(max_length=50, null=False, blank=False)
    description= models.TextField(null=True)
    start_date= models.DateField(blank=False, null=False)
    end_date= models.DateField()

    def __str__(self) -> str:
        return f'{self.company}, {self.job}'

class Project(models.Model):

    title= models.CharField(max_length=50, null=False, blank=False)
    description= models.TextField(null=False, blank=False)
    link= models.CharField(max_length=100, null=False, blank=False)
    image= models.ImageField(upload_to="project", blank=True, null=True)

    def __str__(self) -> str:
        return self.title

class Course(models.Model):

    title= models.CharField(max_length=50, null=False, blank=False)
    info= models.CharField(max_length=50, null=False, blank=False)

    def __str__(self) -> str:
        return self.title