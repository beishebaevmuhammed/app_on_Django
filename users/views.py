from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from carts.models import Cart
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f'{request.user.username}, Вы успешно авторизовались')

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST('next'))

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            messages.success(request, f'{request.user.username}, Вы успешно зарегистрировались')
            return HttpResponseRedirect(reverse('main:index'))

    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home - Регистрация',
        'form': form

    }
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST,
                               instance=request.user,
                               files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно отредактировали профиль')
            return HttpResponseRedirect(reverse('users:profile'))

    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'title': 'Home - Профиль',
        'form': form
    }
    return render(request, 'users/profile.html', context)


def users_cart(request):
    return render(request, 'users/users_cart.html')


@login_required
def logout(request):
    messages.success(request, f'{request.user.username}, Вы вышли из аккаунта')
    auth.logout(request)
    return redirect(reverse('main:index'))
