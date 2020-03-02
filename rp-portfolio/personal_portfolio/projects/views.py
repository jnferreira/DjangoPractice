from django.shortcuts import render, redirect
from .models import Project

from .forms import ProjectForm, AuthForm, UploadFileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout

from django.core.paginator import Paginator

from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/home/nunoferreira/Desktop/django_practice/rp-portfolio/personal_portfolio/projects/static') 

def handle_uploaded_file(f):
    with open('/home/nunoferreira/Desktop/django_practice/rp-portfolio/personal_portfolio/projects/static', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Create your views here.
def project_index(request):

    print(request.user.get_username())

    if request.user.is_authenticated:
        username = request.user.get_username()
    else:
        username = 'John Doe'


    projects = Project.objects.all()

    paginator = Paginator(projects, 5)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {

        'projects': projects,
        'page_obj': page_obj,
        'username': username

    }

    return render(request, 'projects/project_index.html', context)

def project_detail(request, pk):

    # if not request.user.is_authenticated:
    #     return redirect('auth')

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

            myfile = request.FILES['photo']

            filename = fs.save(myfile.name, myfile)

            uploaded_file_url = fs.url(filename)

            handle_uploaded_file(request.FILES['photo'])
            
            project = Project(

                title=form.cleaned_data["title"],

                description=form.cleaned_data["description"],

                technology=form.cleaned_data["technology"],

                photo=uploaded_file_url

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
    return redirect('project_index')
    