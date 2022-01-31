opcao = 999

print(' ---Conversor de Medidas--- ')
print('Escolha uma das opções abaixo')

print('-' * 30)
print('Dimensão')
print('   1-área')
print('   2-comprimento')
print('   3-volume')
print('.' * 30)
print('Mecânica e Movimento')
print('   4-IMC')
print('   5-massa')
print('   6-velocidade')
print('.' * 30)
print('Outros')
print('   7-tempo')
print('   8-temperatura')
print('   9-moeda')
print('.' * 30)
print('Digite 0 para Sair')
print('-' * 30)


while opcao != 0:
    o = str(input('O que você quer converter: '))

    # validar a entrada da opção para outros tipos de variáveis
    while o.isnumeric() != True:
        print('Por favor, digite uma opção válida.')
        o = str(input('O que você quer converter: '))
    opcao = int(o)  

    # validar a entrada da opção para opções não existentes
    if opcao > 9:
        print('Você não escolheu uma opção válida. Digite uma opção válida.')
        print('~' * 65)

                

# Índice de massa corporal (IMC)
    if opcao == 4:
        print('IMC (Índice de massa corporal)\n')

        # validar a entrada da opção para outros tipos de variáveis
        a = str(input('Digite sua altura em m(metros): ')).strip()
        while a.isalpha() == True or a == '' or a.isnumeric() == False and a.isalnum() == True:
            print('Por favor, digite um valor válido.')
            a = str(input('Digite sua altura em m(metros): ')).strip()
        a = a.replace(',', '.')
        altura = float(a)    
        
        # validar a entrada da opção para outros tipos de variáveis     
        p = str(input('Digite seu peso em kg(kilos): ')).strip()
        while p.isalpha() == True or p == '' or p.isnumeric() == False and p.isalnum() == True:
            print('Por favor, digite um valor válido.')
            p = str(input('Digite seu peso em kg(kilos): ')).strip()
        p = p.replace(',', '.')
        peso = float(p)
        
        imc = peso / altura ** 2
        
        print(f'O IMC (Índice de massa corporal) é: {imc:.1f} => ', end='')
        
        if imc < 17:
            print("Você está muito abaixo do peso")
        elif imc <= 18.49:
            print("Você está abaixo do peso")
        elif imc <= 24.99:
            print("Você está saudável")
        elif imc <= 29.99:
            print("Você está acima do peso")
        elif imc <= 34.99:
            print("Você está com obesidade grau I")
        else:
            print("Você está com obesidade grau II")

    print('~' * 65)
            
# moedas
    if opcao == 9:
        print('\n  --------- Moedas --------- ')
        print('Escolha uma das opções abaixo')

        print('-' * 30)
        print('   1-dolar')
        print('   2-euro')
        print('   3-libra')
        print('   9-sair')
        print('-' * 30)

        opcao_moeda = 999
        while opcao_moeda != 9:
            om = str(input('Qual MOEDA você quer converter: '))

            # validar a entrada da opção para outros tipos de variáveis
            while om.isnumeric() != True:
                print('Por favor, digite uma opção válida.')
                om = str(input('Qual MOEDA você quer converter: '))
            opcao_moeda = int(om)
            
            # validar a entrada da opção para opções não existentes
            if opcao_moeda > 9 or opcao_moeda > 3 and opcao_moeda < 9 or opcao_moeda == 0:
                print('Você não escolheu uma opção válida. Digite uma opção válida.')
                print('~' * 65)
                
            if opcao_moeda == 1:
                # validar a entrada da opção para outros tipos de variáveis
                
                real = float(input('Qual o valor que você deseja converter em DOLAR? R$ '))
                cotacao_dia_dolar = float(input('Qual é a cotação do dia? U$$: '))
                dolar = real / cotacao_dia_dolar
                print(f'Com R$ {real:.2f} você pode comprar U$$ {dolar:.2f}.')
                print('.' * 30)

            elif opcao_moeda == 2:
                # validar a entrada da opção para outros tipos de variáveis
                
                real = float(input('Qual o valor que você deseja converter em EURO? R$ '))
                cotacao_dia_euro = float(input('Qual é a cotação do dia? U$$: '))
                euro = real / cotacao_dia_euro
                print(f'Com R$ {real:.2f} você pode comprar €$ {euro:.2f}.')
                print('.' * 30)

            elif opcao_moeda == 3:
                # validar a entrada da opção para outros tipos de variáveis
                
                real = float(input('Qual o valor que você deseja converter em LIBRA? R$ '))
                cotacao_dia_libra = float(input('Qual é a cotação do dia? U$$: '))
                libra = real / cotacao_dia_libra
                print(f'Com R$ {real:.2f} você pode comprar £$ {libra:.2f}.')
                print('.' * 30)

        