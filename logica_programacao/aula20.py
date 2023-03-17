primeiro_valor = input('Digite um valor:')
segundo_valor = input('Digite outro valor:')


# MINHA RESPOSTA
# if primeiro_valor > segundo_valor:
#     print(primeiro_valor , 'é maior que' ,segundo_valor)
# elif primeiro_valor == segundo_valor:
#     print('Os valores são iguais')
# else:
#     print(segundo_valor, 'é maior que' , primeiro_valor)


# RESPOSTA DO PROFESSOR

if primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor=} é maior ou igual que {segundo_valor=}')
else:
    print(f'{segundo_valor=} é maior que {primeiro_valor=}')
