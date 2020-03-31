import random
dinheiro = 100
print ('Você tem R$ {0}'. format (dinheiro))
aposta = int(input('Quanto você gostaria de apostar? '))

while aposta != 0:
    if aposta <= dinheiro:
        print ('FASE: COME OUT')
        print ('Suas apostas são as seguintes:')
        print ('Pass Line Bet')
        print ('Field')
        print ('Any Craps')
        print ('Twelve')
        escolha = str(input('Em qual você gostaria de apostar? '))

# PASS LINE BET - COME OUT
        if escolha == 'Pass Line Bet':
            soma_gerada = random.randint(2,12)
            if (soma_gerada == 7 or soma_gerada == 11):
                print ('A soma é de {0}'.format(soma_gerada))
                dinheiro = dinheiro + aposta
                print ('Parabéns! Agora você tem R$ {0}'. format (dinheiro))
                aposta = int(input('Quanto você gostaria de apostar? '))
            elif (soma_gerada == 2 or soma_gerada == 3 or soma_gerada == 12):
                print ('A soma é de {0}'.format(soma_gerada))
                dinheiro = dinheiro - aposta
                print ('Não foi dessa vez… Agora você tem R$ {0}'. format (dinheiro))
                if dinheiro > 0:
                    aposta = int(input('Quanto você gostaria de apostar? '))
                else:
                    print ('Você perdeu R${0}'.format(aposta))
# PASS LINE BET - POINT
            else:
                point = soma_gerada
                print ('Passou para a FASE POINT')
                print ('O seu point é de: {0}'.format(point))
                print ('Sua aposta se mantém!')
                soma_gerada = random.randint(2,12)
                while soma_gerada != point and soma_gerada != 7:
                        soma_gerada = random.randint(2,12)
                        print (soma_gerada)
                if soma_gerada == point:
                    print ('A soma é de {0}'.format(soma_gerada))
                    dinheiro = dinheiro + aposta
                    print ('Parabéns! Agora você tem R$ {0}'. format (dinheiro))
                    aposta = int(input('Quanto você gostaria de apostar? '))
                else: 
                    print ('A soma é de {0}'.format(soma_gerada))
                    print ('Que pena! Você perdeu tudo! Sorte na próxima vez...')
                    dinheiro = 0
                    aposta = 0
                    
# FIELD
        elif escolha == 'Field':
            soma_gerada = random.randint(2,12)
            if soma_gerada == 2 :
                print ('A soma é de {0}'.format(soma_gerada))
                dinheiro = dinheiro + (aposta * 2)
                print ('Parabéns! Agora você tem R$ {0}'. format (dinheiro))
                aposta = int(input('Quanto você gostaria de apostar? '))
            elif soma_gerada == 12:
                print ('A soma é de {0}'.format(soma_gerada))
                dinheiro = dinheiro + (aposta * 3)
                print ('Parabéns! Agora você tem R$ {0}'. format (dinheiro))
                aposta = int(input('Quanto você gostaria de apostar? '))
            elif soma_gerada == 5 or soma_gerada == 6 or soma_gerada == 7 or soma_gerada == 8:
                print ('A soma é de {0}'.format(soma_gerada))
                print ('Que pena! Você perdeu tudo!')
                dinheiro = 0
                aposta = 0
            else:
                print ('A soma é de {0}'.format(soma_gerada))
                dinheiro = dinheiro + aposta
                print ('Parabéns! Agora você tem R$ {0}'. format (dinheiro))
                aposta = int(input('Quanto você gostaria de apostar? '))

# ANY CRAPS
        elif escolha == 'Any Craps':
            soma_gerada = random.randint(2,12)
            if soma_gerada == 2 or soma_gerada == 3 or soma_gerada == 12:
                print ('A soma é de {0}'.format(soma_gerada))
                dinheiro = dinheiro + (aposta * 7)
                print ('Parabéns! Agora você tem R$ {0}'. format (dinheiro))
                aposta = int(input('Quanto você gostaria de apostar? '))
            else:
                print ('A soma é de {0}'.format(soma_gerada))
                dinheiro = dinheiro - aposta
                print ('Não foi dessa vez… Agora você tem R$ {0}'. format (dinheiro))
                if dinheiro > 0:
                    aposta = int(input('Quanto você gostaria de apostar? '))
                else:
                    print ('Você perdeu!')

# TWELVE
        else:
            soma_gerada = random.randint(2,12)
            if soma_gerada == 12:
                print ('A soma é de {0}'.format(soma_gerada))
                dinheiro = dinheiro + (aposta * 30)
                print ('Parabéns! Agora você tem R$ {0}'. format (dinheiro))
                aposta = int(input('Quanto você gostaria de apostar? '))
            else:
                print ('A soma é de {0}'.format(soma_gerada))
                dinheiro = dinheiro - aposta
                print ('Não foi dessa vez… Agora você tem R$ {0}'. format (dinheiro))
                if dinheiro > 0:
                    aposta = int(input('Quanto você gostaria de apostar? '))
                else:
                    print ('Você perdeu!')
    else:
        aposta = False