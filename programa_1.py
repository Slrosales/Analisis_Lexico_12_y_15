import re

def validar_placa(placa):
  veri = re.fullmatch('[a-z,A-Z]{3}[0-9]{3}', placa)
  if veri:
      return print('Placa válida')
  else:
      return print('Placa inválida')

while True:
  placa = input("Introduzca la placa a verificar: ")
  validar_placa(placa)