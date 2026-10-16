from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CustomUserCreationForm, ProjectForm
from .models import ProjectModel


# <--- Home Page --->
def home_view(request):
  projects = ProjectModel.objects.all()
  return render(request, 'home.html', {'projects': projects})


# <--- Registration --->
def register_view(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('project_list')
  else:
    form = CustomUserCreationForm()
  return render(request, 'register.html', {'form': form})


# <--- Login View --->
def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('project_list')
  else:
    form = AuthenticationForm()
  return render(request, 'login.html', {'form': form})


# <--- Project List View --->
@login_required
def project_list_view(request):
  if request.user.is_superuser or request.user.is_staff:
    projects = ProjectModel.objects.all()
  else:
    projects = ProjectModel.objects.filter(created_by=request.user)
  return render(
      request, 'project_list.html', {'projects': projects}
  )


# <--- Add Project View --->
@login_required
def add_project_view(request):
  if request.method == 'POST':
    form = ProjectForm(request.POST)
    if form.is_valid():
      project = form.save(commit=False)
      project.created_by = request.user
      project.save()
      return redirect('project_list')
  else:
    form = ProjectForm()
  return render(request, 'add_project.html', {'form': form})


# <--- Project Status Update (NotStarted -> InProgress -> Completed) --->
@login_required
def update_status_view(request, pk):
  project = get_object_or_404(ProjectModel, pk=pk)

  # সঠিক স্ট্যাটাস 'NotStarted' চেক করা হলো
  if project.project_status == 'NotStarted':
    project.project_status = 'InProgress'
  elif project.project_status == 'InProgress':
    project.project_status = 'Completed'

  project.save()
  return redirect('project_list')