from django import forms
from django.contrib.auth.forms import UserCreationForm
from.models import CustomUser,ProjectModel


class CustomUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=(
            'username'
            'email'
            'student_name'
            'student_id'
        )


class ProjectForm(forms.ModelForm):

   class Meta:
    model = ProjectModel
    fields = [
        'project_name',
        'project_description',
        'project_status',
        'deadline',
    ]
    widgets = {
        'deadline': forms.DateInput(attrs={'type': 'date'}),
    }
        