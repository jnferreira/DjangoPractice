from django.shortcuts import render, redirect
from .models import Project

from .forms import ProjectForm, AuthForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout

# Create your views here.
def project_index(request):

    if not request.user.is_authenticated:
        return redirect('auth')

    projects = Project.objects.all()

    context = {

        'projects': projects

    }

    return render(request, 'projects/project_index.html', context)

def project_detail(request, pk):

    if not request.user.is_authenticated:
        return redirect('auth')

    project = Project.objects.get(pk=pk)

    context = {

        'project': project

    }

    return render(request, 'projects/project_detail.html', context)

def add_projects(request):
    if not request.user.is_authenticated:
        return redirect('auth')

    form = ProjectForm()

    if request.method == 'POST':

        form = ProjectForm(request.POST)

        if form.is_valid():

            project = Project(

                title=form.cleaned_data["title"],

                description=form.cleaned_data["description"],

                technology=form.cleaned_data["technology"]

            )

            project.save()

            return redirect('project_index')

    context = {

        "form": form

    }
    
    return render(request, 'projects/add_projects.html', context)

def auth(request):

    form = AuthForm()

    if request.method == 'POST':

        form = AuthForm(request.POST)

        if form.is_valid():

            username=form.cleaned_data["username"]

            password=form.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)    
                return redirect('project_index')
            else:
                 
                return redirect('auth')

    context = {

        "form": form

    }         
            
    return render(request, 'projects/auth.html', context)          

def logout_view(request):
    logout(request)
    return redirect('auth')
    