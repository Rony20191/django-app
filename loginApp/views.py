from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm,LoginForm
from .models import Usuario


def index(request):
    return render(request, 'loginApp/base.html')

def login(request):
    form =LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nome_form = form.cleaned_data['nome']
            senha_form = form.cleaned_data['senha']
            teste=Usuario.objects.filter(nome=nome_form,senha=senha_form).first()
            if(teste !=None):
                return render(request, 'loginApp/BemVindo.html', { 'usuario': teste})
            else:
                form = LoginForm()
                return render(request, 'loginApp/login.html', {'sucess': 1, 'form': form})

    elif request.method == 'GET':
        return render(request, 'loginApp/login.html', {'form': form, 'sucess': 0})



def store(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            nome_form = form.cleaned_data['nome']
            sobrenome_form = form.cleaned_data['sobrenome']
            senha_form = form.cleaned_data['senha']

            usuario = Usuario(nome=nome_form, sobrenome=sobrenome_form, senha=senha_form)
            usuario.save()
            form = PostForm()
            return render(request,'loginApp/create.html',{'sucess': 1,'form': form})
    elif request.method == 'GET':
        return render(request, 'loginApp/create.html', {'form': form,'sucess': 0})


def listar(request):
    return render(request, 'loginApp/listar.html', {'usuarios': Usuario.objects.all(),})

def update(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    form = PostForm(instance=usuario)
    if request.method == 'POST':
        form =PostForm(request.POST,instance=usuario)

        if form.is_valid():
            user = form.save(commit=False)
            user.nome = form.cleaned_data['nome']
            user.sobrenome = form.cleaned_data['sobrenome']
            user.senha = form.cleaned_data['senha']
            user.save()
            return redirect('loginApp:listar')
    elif request.method == 'GET':
            form=PostForm(instance=usuario)
            return render(request, 'loginApp/update.html', {'form': form,'usuario':usuario})


def deleteView(request, id):

    usuario = Usuario.objects.filter(id=id).first()
    usuario.delete()
    return redirect('loginApp:listar')
