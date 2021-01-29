from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms.forms import BaseForm, Form
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.utils.translation import ugettext_lazy as _
from core.models import Transfers
from pathlib import Path
from core.forms import SignUpForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer, TransferFieldSerializer


BASE = Path(__file__).resolve().parent.parent
TEMPLATES = Path(BASE / "templates")


def startPage(request):
    return render(request, "base.html")


@login_required()
def home(request):
    money = 50000
    for transaction in Transfers.objects.raw(f"select * from core_transfers where userId={request.user.id}"):
        money = transaction.money

    accountNumber = request.user.id * 1321241212
    data = {"money": money, "accountNumber": accountNumber}
    return render(request, "home.html", context=data)


@user_passes_test(lambda u: u.is_anonymous, login_url="home")
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
        amount = float(request.POST.get("amount"))
        save = request.POST.get("save")

        money = 50000
        for transaction in Transfers.objects.raw(f"select * from core_transfers where userId={request.user.id}"):
            money = float(transaction.money)

        if (transferTo == transferFrom) or (int(transferFrom) != int(request.user.id) * 1321241212) \
                or (save != "true") or (amount > money):
            return redirect("home")
        else:
            transfers = Transfers(userId=userId, transferFrom=transferFrom, transferTo=transferTo, amount=amount, money=money-amount)
            transfers.save()
            return render(request, "transactionComplete.html")

    return render(request, "bankForm.html")


@login_required()
def transactionsHistory(request):
    transactions = []
    for t in Transfers.objects.raw(f"select * from core_transfers where userId={request.user.id}"):
        transactions.append([t.transferFrom, t.transferTo, t.amount, t.money])
    return render(request, "transactionsHistory.html", {"transactions": transactions})


@user_passes_test(lambda u: u.is_anonymous, login_url="home")
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


@login_required()
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
        return redirect("home")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "changePassword.html", {"form": form})


class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HelloWorldView(APIView):
    def get(self, request):
        return Response(data={"hello": "world"}, status=status.HTTP_200_OK)


class transactions(APIView):
    def get(self, request):
        transactions = []
        for t in Transfers.objects.raw(f"select * from core_transfers where userId={request.user.id}"):
            transactions.append([t.transferFrom, t.transferTo, t.amount, t.money])
        return Response(data={"transactions": transactions}, status=status.HTTP_200_OK)


class transferApi(APIView):
    def post(self, request, format="json"):
        serializer = TransferFieldSerializer(data=request.data)
        if serializer.is_valid():
            transferFrom = serializer.data["transferFrom"]
            transferTo = serializer.data["transferTo"]
            amount = serializer.data["amount"]
            print("Keku: ", transferFrom, transferTo, amount)
            try:
                money = Transfers.objects.get(userId=request.user.id)
            except:
                money = 50000
            try:
                transfers = Transfers(userId=request.user.id, transferFrom=transferFrom, transferTo=transferTo, amount=amount,
                                      money=money - amount)
                transfers.save()
                return Response(data="Transfer complete successfully", status=status.HTTP_201_CREATED)
            except:
                return Response(data="Transfer not completed", status=status.HTTP_400_BAD_REQUEST)
