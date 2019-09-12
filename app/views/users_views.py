from django.shortcuts import render


def sign_up(request):
    return render(request, 'users/form_user.html')
