<div align="center">
  <h1>
     Análisis Léxico
  </h1>

[![GitHub Slrosales](https://img.shields.io/badge/by-Slrosales-purple)](https://github.com/Slrosales)
[![GitHub jfbenitezz](https://img.shields.io/badge/by-jfbenitezz-blue)](https://github.com/jfbenitezz)
[![GitHub lellerena](https://img.shields.io/badge/by-lellerena-red)](https://github.com/Rubens1414)
[![GitHub JuandiGo1](https://img.shields.io/badge/by-JuandiGo1-green)](https://github.com/lunajulio)

</div>

Este repositorio contiene dos programas en Python diseñados para validar matrículas de vehículos y direcciones en un formato común en Barranquilla. Ambos programas utilizan expresiones regulares para validar los formatos de entrada y mostrar los resultados correspondientes.

## Contenido

- **Validación de Matrículas de Vehículos (Punto 12)**
- **Validación de Direcciones (Punto 15)**

## 1. Validación de Matrículas de Vehículos

### Descripción

Este programa valida si una matrícula de vehículo sigue el formato de tres letras seguidas por tres dígitos (XXXNNN). Acepta tanto letras mayúsculas como minúsculas y verifica que la matrícula tenga exactamente seis caracteres en total.

### Salida Esperada

- **Placa válida**: Si la matrícula cumple con el formato correcto.
- **Placa inválida**: Si la matrícula no cumple con el formato.

### Expresión Regular Utilizada

- `[a-z,A-Z]{3}`: Captura tres letras (mayúsculas o minúsculas).
- `[0-9]{3}`: Captura tres dígitos.

### Ejecución

1. Abre el archivo `programa_1.py`.
2. Ejecuta el código.
3. Utiliza un loop con la función `validar_placa(placa)` para realizar múltiples consultas desde la consola.
4. Observa los resultados: "Placa válida" o "Placa inválida".
5. Detén el programa cuando lo desees.

### Pruebas de Ejemplo

- `ABC123` - Placa válida.
- `abc123` - Placa válida.
- `AB1234` - Placa inválida.
- `A1B2C3` - Placa inválida.

## 2. Validación de Direcciones

### Descripción

Este programa valida y desglosa direcciones comunes en Barranquilla, siguiendo un formato específico que incluye un tipo de vía (Cra, Cl, Tr, Diag), seguido de números y letras para la vía y el predio.

### Expresión Regular Utilizada

- `\s*`: Captura espacios opcionales.
- `(Cra|Cl|Tr|Diag)\.?`: Captura la abreviatura de la vía (Cra, Cl, Tr, Diag).
- `([0-9]+[a-z,A-Z]?)`: Captura el número y posible letra de la vía.
- `(No\.?\s*|#)?`: Captura opcionalmente 'No.' o '#' seguido de espacios.
- `([0-9]+[a-z,A-Z])`: Captura el número del predio.
- `\s*-?\s*([0-9]+)`: Captura un guion opcional seguido del número del predio.

### Ejecución

1. Abre el archivo `programa_2.py`.
2. Ejecuta el código.
3. Utiliza un loop con la función `validar_direccion(dir)` para realizar múltiples consultas desde la consola.
4. Observa los resultados que mostrarán los componentes de la dirección o indicarán "Dirección inválida" si no coincide con el formato.
5. Detén el programa cuando lo desees.

### Pruebas de Ejemplo

- `Cra. 47B No. 74C-45` - Dirección válida.
- `Cl 52 No. 21-15` - Dirección inválida.
- `Tr 10A No. 30B50` - Dirección válida.
- `Diag 75 20g-10` - Dirección válida.
- `Cra. 15 30A` - Dirección inválida.

## Requisitos

- Python instalado en tu sistema.
- Un editor de texto o IDE como Visual Studio Code para ejecutar los scripts.

