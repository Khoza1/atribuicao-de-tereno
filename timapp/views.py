from django.shortcuts import render, redirect
from .models import Terreno, RecursoNatural, Documento,ModeloExpiravel,SeuModelo
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .forms import TerrenoForm, RecursoNaturalForm, DocumentoForm
#from celery import shared_task
from django.utils import timezone


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


from django.shortcuts import render

def map_view(request):
    # Você pode passar dados do banco de dados ou qualquer outro local para exibir no mapa
    parcelas = [
        {
            'nome': 'Parcela 1',
            'latitude': 12.9716,
            'longitude': 77.5946,
        },
        {
            'nome': 'Parcela 2',
            'latitude': 13.0827,
            'longitude': 80.2707,
        },
    ]

    return render(request, 'map.html', {'parcelas': parcelas})



def index(request):
    # Página inicial do sistema
    return render(request, 'index.html')

"""F
####
#@shared_task
def excluir_modelos_expirados():
    agora = timezone.now()
    limite_tempo = agora - timezone.timedelta(hours=24)
    modelos_expirados = ModeloExpiravel.objects.filter(data_criacao__lt=limite_tempo)
    modelos_expirados.delete()
"""



def excluir_modelo_apos_24_horas(request, modelo_id):
    try:
        from django.utils import timezone
        
        modelo = SeuModelo.objects.get(id=modelo_id)
        agora = timezone.now()

        # Verifique se o modelo tem mais de 24 horas
        diferenca_tempo = agora - modelo.data_de_criacao  # Subtrai a data de criação do modelo da data atual
        horas_passadas = diferenca_tempo.total_seconds() / 120 #(3600)=24  # Converte a diferença de tempo para horas

        if horas_passadas >= 2:
            # Se passaram 24 horas, exclua o modelo
            modelo.delete()
            return HttpResponse("O modelo foi excluído após 24 horas.")
        else:
            return HttpResponse("Ainda não passaram 24 horas.")
    except SeuModelo.DoesNotExist:
        return HttpResponse("Modelo não encontrado.")





