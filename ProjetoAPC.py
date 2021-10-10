status_config = False
areas = []
totalPessoas = 0

'''AQUI ESTÁ AS DEFINIÇÕES DAS FUNÇÕES'''


def verificaMesa(area):
    """Função para verificação de mesas ocupadas"""
    contador_ocupada = 0
    for mesa in area['mesas']:
        if mesa['ocupada']:
            contador_ocupada += 1
    return contador_ocupada


def fechamento():
    """Aqui é definido o comando 5 (Fechamento do Restaurante)"""
    print('Restaurante fechado.')
    print('Balanco final de mesas:')
    for area in areas:
        totalDeMesasECadeiras(area)
    print(f"Um total de {totalPessoas} pessoas visitaram o restaurante hoje.")
    print(f"Bom descanso!")


def comando1():
    """Aqui é definido o comando 1"""

    texto = input()
    lista_aux = texto.split()
    area = lista_aux[-1]
    qtdPessoas = int(lista_aux[4])
    area = buscarArea(area)
    ocuparMesa(qtdPessoas, area)


def comando2():
    """Aqui é definido o comando 2"""
    for area in areas:
        print(f'{area["nome"]}: ({verificaMesa(area)} de {len(area["mesas"])} mesas)')


def comando3():
    """Aqui é definido o comando 3"""

    for area in areas:
        cadeiras_ocupadas = 0
        cadeiras_totais = 0
        for mesa in area['mesas']:
            if mesa['ocupada']:
                cadeiras_ocupadas += mesa['ocupantes']
            cadeiras_totais += mesa['cadeiras']
        print(f"{area['nome']}: ({cadeiras_ocupadas} de {cadeiras_totais} pessoas)")


def comando4():
    """Aqui é definido o comando 4"""
    string = input()

    op1 = 'adicionar'  # Variável para verificação de operação desejada
    op2 = 'remover'  # Variável para verificação de operação desejada

    """Aqui é feita a verificação da operação desejada pelo usuário"""

    if op1 in string:  # Se for adicionar, será feita essa parte
        lista_aux = string.split()
        mesa = int(lista_aux[3])
        cadeiras = int(lista_aux[6])
        area = lista_aux[-1]
        area = buscarArea(area)
        for _ in range(mesa):
            mesa = criarMesa(cadeiras)
            area['mesas'].append(mesa)

        print(f"{mesa} mesas de {cadeiras} cadeiras adicionadas com sucesso na area {area}.")
        area['mesas'].sort(key=lambda mesa: mesa['cadeiras'])

    elif op2 in string:  # Se for remover, será feita essa parte
        lista_aux = string.split()
        mesa = int(lista_aux[3])
        cadeiras = int(lista_aux[6])
        area = lista_aux[-1]
        area = buscarArea(area)
        removerMesasDaArea(area, mesa, cadeiras)
        print(f"{mesa} mesas de {cadeiras} cadeiras removidas com sucesso na area {area}.")


def atendimento():
    """Função para o atendimento"""
    status_atendimento = True
    while status_atendimento:

        op = int(input())
        if op == 1:
            # aqui fica comando 1
            comando1()
            verificarOcupacao()
        elif op == 2:
            # aqui fica comando 2
            comando2()
            verificarOcupacao()
        elif op == 3:
            # aqui fica comando 3
            comando3()
            verificarOcupacao()
        elif op == 4:
            # aqui fica comando 4
            comando4()
            verificarOcupacao()
        elif op == -1:
            # aqui fica o fechamento
            fechamento()
            status_atendimento = False


def ocuparMesa(qtdPessoas, area):
    """Essa função serve tanto para levar os clientes até a mesa quanto para designar o tempo de permanência"""
    mesas = area['mesas']
    comandosRestantes = (2 * qtdPessoas) + 2
    clienteEstabelecido = False
    for mesa in mesas:  # Aqui é feita a verificação das mesas na area desejada
        if mesa['cadeiras'] >= qtdPessoas and not mesa['ocupada']:  # Se conseguir alocar o grupo, fará o seguinte código
            mesa['ocupantes'] = qtdPessoas
            mesa['ocupada'] = True
            mesa['comandosRestantes'] = comandosRestantes
            print(f'Um grupo de {qtdPessoas} pessoas ocupou uma mesa de {mesa["cadeiras"]} lugares na area {area["nome"]}.')
            global totalPessoas
            totalPessoas += qtdPessoas
            clienteEstabelecido = True
            break

    if not clienteEstabelecido:  # Se não conseguir alocar, irá imprimir essa mensagem
        print('Nao foi possivel levar o grupo de clientes para uma mesa.')


def totalDeMesasECadeiras(area):
    """Essa função recebe a áreas do restaurante e imprime o total de mesas e cadeiras em cada uma delas"""
    global qtdCadeiras
    print(area['nome'] + ':')
    mesas = area['mesas']
    mesasEQuantidades = {}
    for mesa in mesas:
        qtdCadeiras = mesa['cadeiras']
        try:
            mesasEQuantidades[qtdCadeiras] += 1
        except KeyError:
            mesasEQuantidades[qtdCadeiras] = 1

    chavesDeCadeiras = mesasEQuantidades.keys()

    for chave in chavesDeCadeiras:
        qtdMesas = mesasEQuantidades[chave]
        print(f" {qtdMesas} mesas de {qtdCadeiras} cadeiras.")


def verificarOcupacao():
    """Essa função serve para verificar a ocupação e calcular o tempo de permanencia de cada grupo"""
    for area in areas:
        mesas = area['mesas']
        for mesa in mesas:
            if mesa['ocupada']:
                mesa['comandosRestantes'] -= 1
                if mesa['comandosRestantes'] == 0:
                    mesa['ocupada'] = False
                    mesa['ocupantes'] = 0


def criarMesa(qtdCadeiras):
    """Função para criação de uma mesa que recebe uma quantidade de cadeiras"""
    mesa = {'cadeiras': qtdCadeiras, 'ocupantes': 0, 'ocupada': False, 'comandosRestantes': 0}
    return mesa


def removerMesasDaArea(area, qtdMesas, qtdCadeiras):
    """Função para remover mesas que recebe a área, a quantidade de mesa e a quantidade de cadeiras"""
    contador = 0
    mesas = area['mesas']
    for mesa in mesas:
        if contador == qtdMesas:  # Essa verificação é feita para remover somente a quantidade desejada, e não todas as mesas
            break

        if mesa['cadeiras'] == qtdCadeiras and not mesa['ocupada']:  # Essa é a verificação para a remoção de mesa
            mesas.remove(mesa)
            contador += 1


def buscarArea(nomeDaArea):
    """Aqui fica a função para ver se a area já existe"""
    for area in areas:
        if area['nome'] == nomeDaArea:
            return area
    return None


def configuracao():
    # Aqui é feita a configuração do Restaurante

    linha = input()

    if linha == '--ATENDIMENTO':  # Se o input for --ATENDIMENTO sairá do loop e irá para o atendimento

        global status_config
        status_config = False

    else:

        a, m, c = linha.split()
        m = int(m)
        c = int(c)

        areaEncontrada = buscarArea(a)  # Verifica se a área já existe na lista ou não

        if areaEncontrada is None:
            """Se não existir área com o nome ele irá criar"""
            area = {'nome': a, 'mesas': []}
            for _ in range(m):
                mesa = criarMesa(c)
                area['mesas'].append(mesa)
            area['mesas'].sort(key=lambda mesa: mesa['cadeiras'])
            areas.append(area)

        else:
            """Se existir, ele irá somente adicionar as mesas na area"""
            for _ in range(m):
                mesa = criarMesa(c)
                areaEncontrada['mesas'].append(mesa)
                areaEncontrada['mesas'].sort(key=lambda mesa: mesa['cadeiras'])
    areas.sort(key=lambda area: area['nome'])


"""Aqui é iniciado o programa, com o primeiro input sendo --CONFIGURACAO"""

string = input()

if string == '--CONFIGURACAO':
    status_config = True
    while status_config:
        configuracao()

    else:
        atendimento()
