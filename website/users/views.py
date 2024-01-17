from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            city = form.cleaned_data.get('city')
            tastes = form.cleaned_data.get('tastes')

            output = ""
            for taste in tastes:
                output += taste.name
                output += "; "

            output = output[:len(output)-1]

            msg = f'Спасибо за регистрацию - {username}\n\nПодтвердите свою почту - {email}\nВаш город проживания: {city}\nВаши вкусы: {tastes}'

            messages.success(request, f'Спасибо за регистрацию - {username} | Подтвердите свою почту - {email} | Ваш город проживания: {city} | Ваши вкусы: {output}')
            return redirect('users:login')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('users:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)
