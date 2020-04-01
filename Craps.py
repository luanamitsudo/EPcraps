import random
import time
from colorama import Fore, Back, Style 
dinheiro = 100
print ('Você tem R$ {0}'. format (dinheiro))
time.sleep(0.7)
aposta = int(input('Quanto você gostaria de apostar? '))

while aposta != 0:
    if aposta <= dinheiro:
        print('')
        print ('FASE: COME OUT')
        time.sleep(0.7)
        print ('Suas apostas são as seguintes:')
        time.sleep(0.7)
        print (Fore.RED +'    Pass Line Bet')
        time.sleep(0.7)
        print (Fore.YELLOW +'    Field')
        time.sleep(0.7)
        print (Fore.GREEN +'    Any Craps')
        time.sleep(0.7)
        print (Fore.BLUE +'    Twelve')
        time.sleep(0.7)
        escolha = str(input(Fore.WHITE +'Em qual você gostaria de apostar? '))

# PASS LINE BET - COME OUT
        if escolha == 'Pass Line Bet':
            soma_gerada = random.randint(2,12)
            print(Fore.RED + 'APOSTA: PASS LINE BET')
            time.sleep(0.7)
            print('  FASE: COME OUT')
            time.sleep(0.7)
            print(Fore.WHITE + 'Jogando os dados')
            time.sleep(0.7)
            print('  ...')
            time.sleep(0.7)
            print('     ...')
            time.sleep(0.7)
            print('        ...')
            time.sleep(0.7)
            print(Fore.RED + 'A soma foi de {0}!'.format(soma_gerada))
            time.sleep(0.7)
            if (soma_gerada == 7 or soma_gerada == 11):
                dinheiro = dinheiro + aposta
                print (Fore.WHITE +'Parabéns!! Agora você tem R$ {0}'. format (dinheiro))
                time.sleep(0.7)
                aposta = int(input(Fore.WHITE +'Quanto você gostaria de apostar? '))
            elif (soma_gerada == 2 or soma_gerada == 3 or soma_gerada == 12):
                dinheiro = dinheiro - aposta
                print (Fore.WHITE +'Não foi dessa vez… Agora você tem R$ {0}'. format (dinheiro))
                time.sleep(0.7)
                if dinheiro > 0:
                   print('Próxima rodada!') 
                else:
                    print ('Você perdeu R${0}'.format(aposta))
                    break
# PASS LINE BET - POINT
            else:
                point = soma_gerada
                time.sleep(0.7)
                print ('')
                print (Fore.RED + 'Passou para a FASE POINT')
                time.sleep(0.7)
                print (Fore.WHITE + 'O seu point é de: {0}'.format(point))
                time.sleep(0.7)
                print ('Sua aposta se mantém!')
                soma_gerada = random.randint(2,12)
                print('Jogando os dados')
                time.sleep(0.7)
                print('  ...')
                time.sleep(0.7)
                print('     ...')
                time.sleep(0.7)
                print('        ...')
                time.sleep(0.7)
                print(Fore.RED +'A soma foi de {0}!'.format(soma_gerada))
                time.sleep(0.7)
                while soma_gerada != point and soma_gerada != 7:
                        soma_gerada = random.randint(2,12)
                        print (Fore.WHITE + 'Girando os dados...')
                        time.sleep(0.7)
                        print(Fore.RED +'A soma foi de {0}'.format(soma_gerada))
                        time.sleep(0.7)
                if soma_gerada == point:
                    dinheiro = dinheiro + aposta
                    print (Fore.WHITE + 'Parabéns!!! Agora você tem R$ {0}'. format (dinheiro))
                    time.sleep(0.7)
                    print('')
                    aposta = int(input('Quanto você gostaria de apostar? '))
                else: 
                    print (Fore.WHITE + 'Que pena! Você perdeu tudo! Sorte na próxima vez...')
                    dinheiro = 0
                    aposta = 0
                    
# FIELD
        elif escolha == 'Field':
            soma_gerada = random.randint(2,12)
            print(Fore.YELLOW + 'APOSTA: FIELD')
            time.sleep(0.7)
            print(Fore.WHITE + 'Jogando os dados')
            time.sleep(0.7)
            print('  ...')
            time.sleep(0.7)
            print('     ...')
            time.sleep(0.7)
            print('        ...')
            time.sleep(0.7)
            print (Fore.YELLOW + 'A soma é de {0}'.format(soma_gerada))
            time.sleep(0.7)
            if soma_gerada == 2 :
                dinheiro = dinheiro + (aposta * 2)
                print (Fore.WHITE + 'Parabéns! Agora você tem R$ {0}'. format (dinheiro))
                time.sleep(0.7)
                print('')
                aposta = int(input('Quanto você gostaria de apostar? '))
            elif soma_gerada == 12:
                dinheiro = dinheiro + (aposta * 3)
                print (Fore.WHITE +'Parabéns! Agora você tem R$ {0}'. format (dinheiro))
                time.sleep(0.7)
                print('')
                aposta = int(input('Quanto você gostaria de apostar? '))
            elif soma_gerada == 5 or soma_gerada == 6 or soma_gerada == 7 or soma_gerada == 8:
                print (Fore.WHITE + 'Que pena! Você perdeu tudo!')
                dinheiro = 0
                aposta = 0
            else:
                dinheiro = dinheiro + aposta
                print (Fore.WHITE +'Parabéns! Agora você tem R$ {0}'. format (dinheiro))
                time.sleep(0.7)
                print('')
                aposta = int(input('Quanto você gostaria de apostar? '))

# ANY CRAPS
        elif escolha == 'Any Craps':
            soma_gerada = random.randint(2,12)
            print(Fore.GREEN + 'APOSTA: ANY CRAPS')
            time.sleep(0.7)
            print(Fore.WHITE + 'Jogando os dados')
            time.sleep(0.7)
            print('  ...')
            time.sleep(0.7)
            print('     ...')
            time.sleep(0.7)
            print('        ...')
            time.sleep(0.7)
            print (Fore.GREEN + 'A soma é de {0}'.format(soma_gerada))
            time.sleep(0.7)
            if soma_gerada == 2 or soma_gerada == 3 or soma_gerada == 12:
                dinheiro = dinheiro + (aposta * 7)
                print (Fore.WHITE + 'Parabéns! Agora você tem R$ {0}'. format (dinheiro))
                time.sleep(0.7)
                print('')
                aposta = int(input('Quanto você gostaria de apostar? '))
            else:
                dinheiro = dinheiro - aposta
                print (Fore.WHITE + 'Não foi dessa vez… Agora você tem R$ {0}'. format (dinheiro))
                if dinheiro > 0:
                    print('')
                    aposta = int(input('Quanto você gostaria de apostar? '))
                else:
                    print ('Você perdeu!')

# TWELVE
        else:
            soma_gerada = random.randint(2,12)
            print(Fore.BLUE + 'APOSTA: TWELVE')
            time.sleep(0.7)
            print(Fore.WHITE + 'Jogando os dados')
            time.sleep(0.7)
            print('  ...')
            time.sleep(0.7)
            print('     ...')
            time.sleep(0.7)
            print('        ...')
            time.sleep(0.7)
            print (Fore.BLUE + 'A soma é de {0}'.format(soma_gerada))
            time.sleep(0.7)
            if soma_gerada == 12:
                dinheiro = dinheiro + (aposta * 30)
                print (Fore.WHITE +'Parabéns! Agora você tem R$ {0}'. format (dinheiro))
                print('')
                aposta = int(input('Quanto você gostaria de apostar? '))
            else:
                dinheiro = dinheiro - aposta
                print (Fore.WHITE +'Não foi dessa vez… Agora você tem R$ {0}'. format (dinheiro))
                if dinheiro > 0:
                    print('')
                    aposta = int(input('Quanto você gostaria de apostar? '))
                else:
                    print ('Você perdeu!')      
    else:
        aposta = False