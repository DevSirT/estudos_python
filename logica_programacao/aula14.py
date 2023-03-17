a = 'A'
b = 'B'
c = 1.1
formato = 'a={0} b={1} c={2:.2f}'.format(a, b, c)
formato_1 = 'a={nome1} b={nome2} c={nome3:.2f}'.format(
    nome1=a, nome2=b, nome3=c)  # parâmetro nomeado

print(formato)
print(formato_1)
