# Sistema de cadastro de turmas
AREAS_VALIDAS = ["Matemática", "História", "Inglês"]
DIAS_VALIDOS = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
TURNOS_VALIDOS = ["M", "N", "T"]


def verificar_dados_inseridos(lista: list, resposta: str) -> bool:
    # Verificar se os dados inseridos pelo usuário realmente estão dentro do escopo do programa.
    if resposta not in lista:
        print("Insira somente uma das opções apresentadas.")
        return False
    else:
        return True


def validar_dados(area, dia, turno):
    # Esta função trata os dados organizando-os em forma de dicionários para que
    dict_area = {'resposta_usuario': area, 'lista_areas': AREAS_VALIDAS}
    dict_dia = {'resposta_usuario': dia, 'lista_areas': DIAS_VALIDOS}
    dict_turno = {'resposta_usuario': turno, 'lista_areas': TURNOS_VALIDOS}
    lista_geral = [dict_area, dict_dia, dict_turno]
    # Esta lista é composta pelo resultado do retorno de cada valor da lista a cima
    lista_resposta = [verificar_dados_inseridos(lista=item['lista_areas'], resposta=item['resposta_usuario']) for item
                      in lista_geral]
    return lista_resposta  # True ou False


# Grupo das turmas já cadastradas
turmas_cadastradas = []


def remover_turma():
    # Verificar se há turmas cadastradas
    if len(turmas_cadastradas) > 0:
        listar_turmas_cadastradas()
        resposta = int(input("Qual turma deseja excluir (nº da turma): ")) - 1
        if resposta < 0 or resposta > len(turmas_cadastradas):
            # Verifica se o número da turma inserido corresponde ao número de turmas cadastradas
            print("Opção inválida.")
            remover_turma()
        else:
            # Remove a turma através do índice
            turmas_cadastradas.pop(resposta)
            print("Turma excluída com sucesso.")
    else:
        print("NÃO HÁ TURMAS CADASTRADAS.")


# Listagem dos dados da turma
def listar_turmas_cadastradas():
    if len(turmas_cadastradas) == 0:
        print("\n\033[1mNão há turmas cadastradas.\033[1m".upper())
    for indice in range(len(turmas_cadastradas)):
        # Estas variáveis são responsáveis apenas para facilitar o entendimento do código
        turma_atual = turmas_cadastradas[indice]
        sub_data = turma_atual['dados_da_materia']
        ##########################################
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
    # Recebe os dados do usuário
    materia = input("Nome da matéria: ").capitalize()
    area = input("Qual área -  matemática | história | inglês: ").capitalize()
    dia = input("Dia - segunda | terça | quarta | quinta | sexta: ").capitalize()
    turno = input("Turno - [M] manhã | [T] tarde | [N] noite: ").upper()

    # Verifica se os dados inseridos estão de acordo com os dados apresentados (Tratamento).
    verificacao_de_dados = validar_dados(area, dia, turno)

    if False in verificacao_de_dados:
        cadastrar_nova_turma()
    else:
        # Formatação dos dados em dicionário
        turma = {"materia": materia, "dados_da_materia": {"area": area, "dia": dia, "turno": turno}}
        # Verifica se já existe uma turma da mesma área cadastrada no mesmo horário.
        ja_existe = verificar(turma)
        if ja_existe:
            print(f"Turma de {area} já cadastrada nesse turno.")
            cadastrar_nova_turma()
        else:
            turmas_cadastradas.append(turma)
            print("Turma cadastrada com sucesso!")


########################################################################################

"""MENU INICIAL"""
# Controla o funcionamento do programa
is_on = True
while is_on:
    # Breve explicação a respeito do funcionamento do programa
    opcao = input(
        "\n\033[1mMenu\033[1m\n[1] - Cadastrar Nova Turma\n[2] - Remover Turma\n[3] - Listar turmas\n[0] - "
        "Sair\nEscolha uma opção: ").strip()

    # Funções a serem executadas dependendo da escolha do usuário.
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
