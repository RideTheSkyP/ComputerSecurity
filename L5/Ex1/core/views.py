from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms.forms import BaseForm, Form
# from core.databaseConnection import Database
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from core.models import Transfers
from bs4 import BeautifulSoup
from pathlib import Path
from django.template import Template, Context


BASE = Path(__file__).resolve().parent.parent
TEMPLATES = Path(BASE / "templates")


def startPage(request):
    return render(request, "base.html")


@login_required()
def home(request):
    return render(request, "home.html")


def loginToAcc(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


@login_required()
def logoutFromAcc(request):
    logout(request)
    return redirect("start")


@login_required()
def statistics(request):
    print(request)


@login_required()
def transfer(request):
    if request.method == "POST":
        userId = request.user.id
        transferFrom = request.POST.get("transferfrom")
        transferTo = request.POST.get("transferto")
        amount = request.POST.get("amount")
        transfers = Transfers(userId=userId, transferFrom=transferFrom, transferTo=transferTo, amount=amount)
        transfers.save()
        return render(request, "error.html")
    return render(request, "bankForm.html")


@login_required()
def transactionsHistory(request):

    transactions = [{"sad", "das", "dsa"}, {"pol", "olp", "lop"}]
    return render(request, "transactionsHistory.html", {"transactions": transactions})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            # db = Database()
            # db.addUser(username, password)
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})
