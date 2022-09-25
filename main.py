turmas_cadastradas = []


def remover_turma():
    listar_turmas_cadastradas()
    resposta = int(input("Qual turma deseja excluir (nº da turma): ")) - 1
    if resposta < 0 or resposta > len(turmas_cadastradas):
        print("Opção inválida.")
        remover_turma()
    else:
        turmas_cadastradas.pop(resposta)
        print("Turma excluída com sucesso.")


# Listagem dos dados da turma
def listar_turmas_cadastradas():
    if len(turmas_cadastradas) == 0:
        print("Não há turmas cadastradas.")
    for indice in range(len(turmas_cadastradas)):
        turma_atual = turmas_cadastradas[indice]
        sub_data = turma_atual['dados_da_materia']
        texto_formatado = f"Turma {indice + 1}:\nMatéria: {turma_atual['materia']}\nÁrea: {sub_data['area']} | " \
                          f"Dia: {sub_data['dia']} | Turno: {sub_data['turno']}\n"
        print(texto_formatado)


"""Esta parte do código é responsável por cadastrar e verificar se a turma já existe na lista"""


def verificar(turma: dict):
    for turma_cadastrada in turmas_cadastradas:
        if turma['dados_da_materia'] == turma_cadastrada['dados_da_materia']:
            return True
        else:
            return False


def cadastrar_nova_turma():
    materia = input("Nome da matéria: ").capitalize()
    area = input("Qual área -  matemática | história | inglês: ").capitalize()
    dia = input("Dia - segunda | terça | quarta | quinta | sexta: ").capitalize()
    turno = input("Turno - [M] manhã | [T] tarde | [N] noite: ").upper()
    # Formatação dos dados em dicionário
    turma = {"materia": materia, "dados_da_materia": {"area": area, "dia": dia, "turno": turno}}
    ja_existe = verificar(turma)
    if ja_existe:
        print(f"Turma de {area} já cadastrada nesse turno.")
        cadastrar_nova_turma()
    else:
        turmas_cadastradas.append(turma)
        print("Turma cadastrada com sucesso!")


########################################################################################


is_on = True
while is_on:
    opcao = input(
        "\nMenu\n[1] - Cadastrar Nova Turma\n[2] - Remover Turma\n[3] - Listar turmas\n[0] - Sair\nEscolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_nova_turma()
    elif opcao == "2":
        remover_turma()
    elif opcao == "3":
        listar_turmas_cadastradas()
    elif opcao == "0":
        is_on = False
    else:
        print("Opção inválida")
