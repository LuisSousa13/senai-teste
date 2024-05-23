def fahrenheit_para_celsius(fahrenheit):
  """
  Converte uma temperatura em graus Fahrenheit para Celsius.

  Argumentos:
    fahrenheit: A temperatura em graus Fahrenheit (float).

  Retorna:
    A temperatura em graus Celsius (float).
  """
  celsius = (fahrenheit - 32) * 5 / 9
  return celsius

# Pede a temperatura em Fahrenheit ao usuário
temperatura_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

# Converte a temperatura para Celsius
temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)

# Mostra a temperatura em Celsius
print(f"A temperatura em Celsius é: {temperatura_celsius:.2f}")