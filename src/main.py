from frota import *


def operar_carro(carro: Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro.acelerar(v, t)
    print('Infos atuais do carro')
    print(carro)


if __name__ == "__main__":
    print('Cadastre o carro 1')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    combustivel = float(input('Digite a quantidade de combustível no tanque: '))
    consumo_medio = float(input('Digite o consumo médio de combustível por km: '))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0, motor=False, consumo_medio=consumo_medio, tanque=combustivel)

    print('Cadastre o carro 2')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    combustivel = float(input('Digite a quantidade de combustível no tanque: '))
    consumo_medio = float(input('Digite o consumo médio de combustível por km: '))

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0, motor=False, consumo_medio=consumo_medio, tanque=combustivel)

    '''
    Controlando o carro até ele atingir 10000 Km
    '''
    while (carro1.odometro < 600 and carro2.odometro < 600) \
            and (carro1.tanque > 0 and carro2.tanque > 0):
        try:
            numero_carro = 0
            while numero_carro not in [1, 2]:
                numero_carro = int(input('Informe o carro [1, 2]:'))
            if numero_carro == 1:
                operar_carro(carro1)
            elif numero_carro == 2:
                operar_carro(carro2)

        except Exception as e:
            print("Erro!")
            print(e)
    if carro1.motor_on: carro1.desligar()
    if carro2.motor_on: carro2.desligar()

    if carro1.odometro >= 600:
        print('O carro 1 venceu a corrida')
    elif carro2.odometro >= 600:
        print('O carro 2 venceu a corrida')
    elif carro1.tanque == 0:
        print('Acabou o tanque do carro 1')
    else:
        print('Acabou o tanque do carro 2')
