from email.policy import default
from django.db import models

class Project(models.Model):
    # self.id 
    project_name = models.CharField(max_length=128, blank=False)
    project_media = models.ImageField()
    project_description = models.TextField(blank=False)
    project_detail = models.TextField()
    project_repo = models.URLField()

    def __str__(self):
        return self.project_name


class Experience(models.Model):
    CHOICES = [
        ('PRF', 'Professional'),
        ('LDR', 'Leadership'),
        ('VLT', 'Volunteer')
    ]

    experience_type = models.CharField(max_length=3, choices=CHOICES, default='PRF')
    experience_name = models.CharField(max_length=128)
    experience_company = models.CharField(max_length=128)
    experience_description = models.TextField()
    experience_start_date = models.DateField()
    experence_end_date = models.DateField()
    experience_skills = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.experience_name

class Certification(models.Model):
    CHOICES = [
        ('CMP', 'Competetion'),
        ('CRS', 'Course'),
        ('VLT', 'Volunteer')
    ]

    certificate_name = models.CharField(max_length=128)
    certificate_issuer = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.certificate_name