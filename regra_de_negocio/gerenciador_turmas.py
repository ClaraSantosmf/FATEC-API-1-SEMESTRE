import json


# Esta função busca informações sobre as turmas a partir de um arquivo JSON e as retorna
def busca_turmas():
    with open("dados/turmas.json", "r", encoding="utf-8") as f:
        turmas_data = json.load(f)
    return turmas_data

def _salvar_turmas(turmas):
    dados = json.dumps(turmas, indent=4)
    with open("dados/turmas.json", "w", encoding="utf-8") as arquivo:
        arquivo.write(dados)
    return True

def editar_turma_svc(id, nome, professor, data_de_inicio):
    turmas = busca_turmas()
    if id in turmas.keys():
        turma = turmas[id]
        turma["nome"] = nome
        turma["professor"] = professor
        turma["data_de_inicio"] = data_de_inicio
        _salvar_turmas(turmas)
        return True
    else:
        return False
# Parâmetro: um dicionário onde cada turma é um par chave-valor
# Retorna:
#   True se a operação for bem sucedida

# Função para criar uma nova turma
def criacao_turma(dados_nova_turma, grupos):
    """
    Dados da nova turma vem no seguinte formato:
    nome: nome da turma
    professor: nome professor
    data_de_inicio: data selecionada
    grupos: uma lista dos grupos que foram selecionados para perteceram a essa turma
    """
    dados_nova_turma_json = json.loads(dados_nova_turma)
    turmas = busca_turmas()

    turma_novo_id = str(len(turmas) + 1)

    nova_turma = {
        "nome": dados_nova_turma_json["nome"],  # Acesse a propriedade "nome" do corpo
        "professor": dados_nova_turma_json[
            "professor"
        ],  # Acesse a propriedade "professor" do corpo
        "data_de_inicio": dados_nova_turma_json[
            "dataInicio"
        ],  # Acesse a propriedade "dataInicio" do corpo
    }
    turmas[turma_novo_id] = nova_turma
    turma_nome = turmas[turma_novo_id]["nome"]
    resposta = {
        "mensagem": f"Criação da turma {turma_nome.capitalize()} realizada com sucesso!",
        "detalhes": [],
    }

    if len(dados_nova_turma_json["grupos"]) >= 1: #Se a lista vier com pelo menos 1 grupo
        for idGrupo in dados_nova_turma_json["grupos"]: #Percorre a lista para pegar cada id
            idGrupo = str( #Transforma o id em str para pode ser comparado com o grupos.json
                idGrupo
            )
            print(f"ID do grupo a ser atualizado: {idGrupo}")
            # Verifique se o ID do grupo existe nos grupos
            if idGrupo in grupos: #pega esse id da lista e procura ele no grupos.json
                print(f"Atualizando grupo {idGrupo} para turma {turma_novo_id}")
                grupo_Nome = grupos[idGrupo]["nome"] #Pega o nome do grupo
                grupos[idGrupo]["turma"] = int(turma_novo_id) # Atualize a propriedade "turma" do grupo com um valor inteiro
                # Cria os detalhes de alterações nos grupos
                resposta["detalhes"].append(
                    f"Adicionado o grupo {grupo_Nome.capitalize()} a turma {turma_nome.capitalize()}"
                ) # Nessa resposta por exemplo: pega o nome do grupo e o nome da turma para dizer que foi feito com sucesso a operacao
            else:
                resposta["detalhes"].append(
                    f"id {grupo_Nome.capitalize()} não encontrado nos grupos"
                )

    # Salve as alterações nos arquivos JSON
    _salvar_turmas(turmas)
    return resposta


def excluir_turma(id):
    turmas = busca_turmas()
    if id in turmas.keys():
        turmas.pop(id)
        _salvar_turmas(turmas)
        return True
    else:
        return False
