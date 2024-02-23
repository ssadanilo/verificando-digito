while True:
    numero_errado = input('Digite um número quebrado utilizando uma vírgula: ').replace(',','.')

    if numero_errado.replace('.','').isdigit():
        numero_corrigido = float(numero_errado)
        print(f'O número infomado é {numero_corrigido}')
        break
    else:
        print('Incorreto! Digite um número')
    
