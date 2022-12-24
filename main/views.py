from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_django
from django.core.paginator import Paginator

from main.models import Categorias, Despesas, Receitas

from datetime import date

# ------------------------------ CADASTRO -------------------------------


def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        first_name = request.POST.get("name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username).first()

        if user:
            return redirect("login")

        user = User.objects.create_user(
            first_name=first_name, email=email, username=username, password=password
        )
        user.save()

        return HttpResponse("usuario cadastrado com sucesso")


# ------------------------------ LOGIN -------------------------------


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)
            return redirect("home")
        else:
            return redirect("login")


# ------------------------------ HOME -------------------------------


@login_required(login_url="ifinance/login/")
def home(request):
    categorias = Categorias.objects.filter(user=request.user)

    despesas = Despesas.objects.filter(user=request.user)
    receitas = Receitas.objects.filter(user=request.user)
    totalReceita = 0
    totalDespesa = 0

    for receita in receitas:
        totalReceita += receita.valor
    for despesa in despesas:
        totalDespesa += despesa.valor

    context = {
        "categorias": categorias,
        "totalReceita": totalReceita,
        "totalDespesa": totalDespesa,
        "totalSaldo": totalReceita - totalDespesa,
    }

    return render(request, "dashboard.html", context)


# ------------------------------ CATEGORIA ------------------------------
# -----------------------------------------------------------------------


@login_required()
def create_category(request):
    name = request.POST.get("name")
    Categorias.objects.create(name=name, user=request.user)

    return redirect("home")


@login_required()
def delete_categoria(request, id):
    categoria = Categorias.objects.filter(id=id).first()
    categoria.delete()

    return redirect("home")


# ------------------------------- RECEITA --------------------------------
# ------------------------------------------------------------------------


@login_required()
def create_receita(request):
    nome = request.POST.get("nome")
    valor = request.POST.get("valor")
    idCategoria = request.POST.get("categoria")
    categoria = Categorias.objects.filter(id=idCategoria).first()
    data = date.today()

    Receitas.objects.create(
        nome=nome, valor=valor, categoria=categoria, data=data, user=request.user
    )

    return redirect("receita")


@login_required()
def receita(request):

    categorias = Categorias.objects.filter(user=request.user)
    receitas = Receitas.objects.filter(user=request.user)

    context = {"receitas": receitas, "categorias": categorias}

    return render(request, "tables.html", context)


@login_required
def delete_receita(request, id):
    receita = Receitas.objects.filter(id=id).first()
    receita.delete()

    return redirect("receita")


# ------------------------------- DESPESA --------------------------------
# ------------------------------------------------------------------------


@login_required()
def create_despesa(request):
    nome = request.POST.get("nome")
    valor = request.POST.get("valor")
    idCategoria = request.POST.get("categoria")
    categoria = Categorias.objects.filter(id=idCategoria).first()
    data = date.today()

    Despesas.objects.create(
        nome=nome, valor=valor, categoria=categoria, data=data, user=request.user
    )

    return redirect("despesa")


@login_required()
def despesa(request):
    categorias = Categorias.objects.filter(user=request.user)
    despesas = Despesas.objects.filter(user=request.user)

    context = {
        "despesas": despesas,
        "categorias": categorias,
    }

    return render(request, "wallet.html", context)


@login_required()
def delete_despesa(request, id):
    despesa = Despesas.objects.filter(id=id).first()
    despesa.delete()

    return redirect("despesa")


# ------------------------------- LOGOUT ---------------------------------
# ------------------------------------------------------------------------


@login_required()
def logout(request):
    logout_django(request)
    return redirect("login")
