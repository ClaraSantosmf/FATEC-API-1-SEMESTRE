from wgsi import HttpResponse, JsonResponse
from regra_de_negocio.service import busca_dados_json


def hola_mundinho(request):
    return HttpResponse("Olá Mundo")


def get_arquivos_json(request):
    dados = busca_dados_json()
    return JsonResponse(dados)


def edit_aluno(request, id):
    return JsonResponse({"message": f"Editando o aluno com ID {id}."})
