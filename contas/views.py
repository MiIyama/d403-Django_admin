from django.shortcuts import render
from .models import Pessoa

def mostrar_formulario_cadastro(request):
  contexto = {'msg': None}
  if request.method == 'POST':
    pessoa = Pessoa()
    pessoa.nome = request.POST['nome']
    pessoa.cpf = request.POST['cpf']
    pessoa.email = request.POST['email']
    pessoa.telefone = request.POST['telefone']
    pessoa.genero = request.POST['genero']
    pessoa.save()
    contexto = {'msg' : 'Aeee parabens'}
  return render(request, 'index.html', contexto)

def mostrar_pessoas(request):
  pessoas = Pessoa.objects.all()

  return render(request, 'pessoas.html', {'dados': pessoas})