def calcular_peso_ideal(altura, sexo):
  """
  Calcula o peso ideal de uma pessoa.

  Args:
    altura: Altura da pessoa em metros.
    sexo: Sexo da pessoa ("homem" ou "mulher").

  Returns:
    Peso ideal da pessoa em kg.
  """

  if sexo == "homem":
    peso_ideal = (72.7 * altura) - 58
  elif sexo == "mulher":
    peso_ideal = (62.1 * altura) - 44.7
  else:
    raise ValueError("Sexo inválido.")

  return peso_ideal

# Exemplo de uso
altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo (homem/mulher): ")

peso_ideal = calcular_peso_ideal(altura, sexo)

print("Seu peso ideal é:", peso_ideal, "kg")