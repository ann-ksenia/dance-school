from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .models import *
from .forms import *
from django.contrib.auth import login as dj_login, logout, login, authenticate
from django.contrib import messages
from django.core.mail import send_mail


def main(request):
    return render(request, 'danceschool/main.html')

def user_login(request):
    if request.user.is_authenticated == True:
        user = request.user
        return render(request, 'danceschool/profile.html', {'user': user})
    else:
        if request.method == 'POST':
            form = UserLoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                dj_login(request, user)
                messages.success(request, 'Успешный вход')

                return redirect('login')
            else:
                messages.error(request, 'Ошибка входа')
        else:
            form = UserLoginForm()
        return render(request, 'danceschool/login.html', {'form': form})

def sign_up(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            dj_login(request, user)
            messages.success(request, 'Успешная регистрация')
            photo = request.FILES['photo']
            phone = form.cleaned_data.get('phone')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            Profile.objects.create(
                user=user,
                photo=photo,
                phone = phone
            )
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'danceschool/sign_up.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def edit(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            photo = request.FILES['photo']
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            request.user.profile.photo = photo
            request.user.profile.phone = phone
            request.user.profile.email = email
            request.user.username = username
            request.user.save()
            request.user.profile.save()
            return redirect('profile')
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
        form.initial['phone'] = request.user.profile.phone
        form.initial['photo'] = request.user.profile.photo
        form.initial['email'] = request.user.profile.email
        form.initial['password1'] = request.user.password
        form.initial['username'] = request.user.username
    return render(request, 'danceschool/edit.html', {'form': form})

class UpdateView(UpdateView):
    model = Profile
    fields = ('photo', 'phone', 'email')
    template_name = 'danceschool/edit.html'

class Update(UpdateView):
    def profile(request):
        if request.method == 'POST':
            user_form = UpUser(request.POST, instance=request.user)
            profile_form = UpProfile(request.POST, request.FILES, instance=request.user.profile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Your profile is updated successfully')
                return redirect(to='login')
        else:
            user_form = UpUser(instance=request.user)
            profile_form = UpProfile(instance=request.user.profile)

        return render(request, 'danceschool/edit.html', {'user_form': user_form, 'profile_form': profile_form})

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'danceschool/password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')


def CheckTicket(request):
    visits = request.user.profile.visits.count()
    visits2 = request.user.profile.ticket.amount
    if (visits2 == visits):
        check = False
    else:
        check = True
    return render(request, 'danceschool/profile.html', check)