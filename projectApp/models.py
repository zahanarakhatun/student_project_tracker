from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    student_name =models.CharField(max_length=100,null=True)
    student_id =models.CharField(max_length=100,null=True)

    def __str__(self):
        return f"{self.username} ({self.username})"


class ProjectModel(models.Model):

    STATUS_CHOICES={
        ('NotStarted', 'Not Started'),
        ('InProgress', 'In Progress'),
        ('Completed', 'Completed'),
    }
    project_name =models.CharField(max_length=200,null=True)
    project_description =models.TextField()
    project_status =models.CharField(max_length=100, choices=STATUS_CHOICES,default='NotStarted',null=True)
    deadline =models.DateField()
    created_by = models.ForeignKey(
      CustomUser, on_delete=models.CASCADE, related_name='projects'
  )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
     return self.project_name