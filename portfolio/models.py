from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class projects(models.Model):
    project_title = CharField(max_length=100)
    project_description = CharField(max_length=1000)
    project_image = CharField(max_length=1000)
    project_link = CharField(max_length=200)
    def __str__(self):
        return self.project_title
    
class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_logo = models.ImageField(upload_to ='images')
    def __str__(self):
        return self.skill_name