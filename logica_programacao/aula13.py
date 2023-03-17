nome = 'Thulio Carlos'
altura = 1.74
peso = 100
imc = peso / (altura * altura)

# f-strings"
linha = (f"{nome} tem{altura: .2f} de altura, pesa {peso}"
         f"quilos e seu IMC é{imc: .2f}")

# Thúlio Carlos tem 1.74 de altura,
# pesa 100 quilos e seu IMC é
# 33.029462280354075


print(linha)
