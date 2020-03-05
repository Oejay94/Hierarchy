from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from customuser.models import CustomUser

from .models import File_or_Folder
from .forms import add_form, login_form, signup_form, create_form

@login_required()
def file_folder_view(request):
    html = 'main.html'
    return render(request, html, {'files': File_or_Folder.objects.filter(user=request.user)})

@login_required()
def add_view(request, id):
    html = 'add_form.html'

    if request.method == 'POST':
        form = add_form(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            File_or_Folder.objects.filter(id=id).create(
                name=data['name'],
                parent=data['category'],
                user=request.user
            )
            return HttpResponseRedirect(reverse('main'))

    else:
        form = add_form()

    return render(request, html, {'form': form})


def create_view(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = create_form(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            File_or_Folder.objects.create(
                name=data['name'],
                user=request.user
            )
            return HttpResponseRedirect(reverse('main'))
    else:
        form = create_form()
    
    return render(request, html, {'form': form})


def login_view(request):
    html = 'login.html'

    if request.method == 'POST':
        form = login_form(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user is not None:
                login(request, user)
                return HttpResponse(reverse('main'))
    else:
        form = login_form()

    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.GET.get('next', '/login/'))


def signup_view(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = signup_form(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = CustomUser.objects.create(
                username=data['username'],
                first_name=data['first_name'],
                password=data['password1']
            )
            login(request, user)
        return HttpResponseRedirect(reverse('main'))
    else:
        form = signup_form()

    return render(request, html, {'form': form})

