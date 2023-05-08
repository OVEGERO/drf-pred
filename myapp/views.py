from django.shortcuts import render
from .logic import modeloSNN
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse

# Create your views here.

@api_view(['GET', 'POST'])
def predecir(request):
    try:
        comentario = request.POST['comentario']
        resul = modeloSNN.modeloSNN.predecirNuevasMuestras(modeloSNN.modeloSNN,Comentario=comentario)
        print('resultado de la prediccion: ' + resul)
        return render(request, 'informe.html', {
            'resul': resul
        })
    except Exception as e:
        return render(request, 'informe.html', {
            'resul': e
        })

@csrf_exempt
@api_view(['GET', 'POST'])
def predecirIOJson(request):
    print(request)
    print('****')
    print(request.body)
    print('****')
    body = json.loads(request.body.decode('utf-8'))
    # Formato de datos de entrada
    comentario = body['comentario']
    resul = modeloSNN.modeloSNN.predecirNuevasMuestras(modeloSNN.modeloSNN,Comentario=comentario)
    data = {'resul': resul}
    resp = JsonResponse(data)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

def home(request):
    return render(request, 'Pages/home.html')

def preguntas(request):
    return render(request, 'Pages/preguntas.html')

def sobre(request):
    return render(request, 'Pages/sobre.html')
