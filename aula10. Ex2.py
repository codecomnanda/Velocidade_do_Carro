#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite
#Programa que eu criei
velocidade_carro = float(input('Qual é a velocidade do carro? '))
if velocidade_carro <=80:
    print('\033[32mVocê está dentro da velocidade permitida!\033[m') #código para colocar cores no terminal de saída
else:
    excesso = velocidade_carro - 80
    multa = excesso * 7
    print(f'\033[31mVocê excedeu a velocidade permitida, por isso, foi multado em {multa:.2f} reais.\033[m')

#Programa do Professor Guanabara
'''velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h.')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}.')
print('Tenha um bom dia! Dirija com segurança!')'''
