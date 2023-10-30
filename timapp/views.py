from django.shortcuts import render, redirect
from .models import Terreno, RecursoNatural, Documento
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .forms import TerrenoForm, RecursoNaturalForm, DocumentoForm


def terreno_list(request):
    terrenos = Terreno.objects.all()
    return render(request, 'terrenos/terreno_list.html', {'terrenos': terrenos})


def terreno_create(request):
    if request.method == 'POST':
        form = TerrenoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('terrenos:terreno_list')
    else:
        form = TerrenoForm()
    return render(request, 'terrenos/terreno_form.html', {'form': form})

def recursos_naturais(request):
    recursos = RecursoNatural.objects.all()
    return render(request, 'recursos/recursos_naturais.html', {'recursos': recursos})

def recurso_natural_create(request):
    if request.method == 'POST':
        form = RecursoNaturalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('terrenos:recursos_naturais')
    else:
        form = RecursoNaturalForm()
    return render(request, 'recursos/recurso_natural_form.html', {'form': form})

def documentos(request):
    docs = Documento.objects.all()
    return render(request, 'documentos/documentos.html', {'documentos': docs})

def documento_create(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('terrenos:documentos')
    else:
        form = DocumentoForm()
    return render(request, 'documentos/documento_form.html', {'form': form})

def gerar_relatorio(request):
    # Lógica para gerar relatório
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio.pdf"'

    # Crie o arquivo PDF usando a biblioteca ReportLab
    buffer = response.content
    p = canvas.Canvas(buffer, pagesize=letter)
    
    # Conteúdo do relatório
    p.drawString(100, 700, "Relatório de Terrenos e Recursos Naturais")
    
    # Adicione informações do banco de dados ao relatório
    terrenos = Terreno.objects.all()
    recursos = RecursoNatural.objects.all()
    
    y = 650
    for terreno in terrenos:
        p.drawString(100, y, f"Proprietário: {terreno.proprietario}")
        y -= 20
    
    for recurso in recursos:
        p.drawString(100, y, f"Recurso Natural: {recurso.nome}")
        y -= 20

    p.showPage()
    p.save()
    buffer.seek(0)
    response.write(buffer.read())

    return response


def index(request):
    # Página inicial do sistema
    return render(request, 'index.html')
