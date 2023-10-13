import json


# Esta função busca informações sobre as turmas a partir de um arquivo JSON e as retorna
def busca_turmas():
    with open("dados/turmas.json", "r", encoding="utf-8") as f:
        turmas_data = json.load(f)
    return turmas_data

def excluir_turma(id):
    turmas = busca_turmas()
    if id in turmas.keys():
        turmas.pop(id)
        salvar_turmas(turmas)
        return True
    else:
        return False