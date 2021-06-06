import account
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from account.models import Account
from account.forms import UserLoginForm
from articles.models import FavouriteArticle


def registration_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_object = Account()
        user_object.email = email
        user_object.set_password(password)
        user_object.phone_number = "+966" + \
            request.POST.get("phone_number")
        user_object.name = request.POST.get("name")
        user_object.date_of_birth = request.POST.get("date_of_birth")
        user_object.national_id = request.POST.get("national_id")
        user_object.save()

        account = authenticate(email=email, password=password)
        login(request, account)
        return redirect('home')
    else:
        return render(request, 'registration.html')


def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')
        else:
            context = {
                'msg': 'Incorrect Data'
            }
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('home')
    else:
        logout(request)
        return redirect('home')


def user_profile_view(request, account_id):
    if not request.user.is_authenticated:
        return redirect('home')
    else:
        account = Account.objects.get(id=account_id)
        favourite_articles = FavouriteArticle.objects.filter(
            account=account)
        context = {"favourite_articles": favourite_articles}
        return render(request, 'profile.html', context)
