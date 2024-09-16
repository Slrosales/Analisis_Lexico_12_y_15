import re

def validar_direccion(dir):
    ver = re.fullmatch(r"\s*(Cra|Cl|Tr|Diag)\.?\s*([0-9]+[a-z,A-Z]?)\s*(No\.?\s*|#)?([0-9]+[a-z,A-Z])\s*-?\s*([0-9]+)\s*", dir)
    if ver:
        print("Dirección:", ver.group(0))  # The entire match
        print("Vía:", ver.group(1))  # Cra, Cl, Tr, Diag
        print("Número de Vía:", ver.group(2))  # First number
        print("Número de Vía Origen Dirección:", ver.group(4))  # Optional No. or #
        print("Número Predio:", ver.group(5))  # Second number
    else:
        print("Dirección inválida")

while True:
  dir = input("Introduzca la dirección a verificar: ")
  validar_direccion(dir)