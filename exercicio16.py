def maior_numero(numero1, numero2):
  """
  Função que retorna o maior número entre dois números.

  Argumentos:
    numero1 (int): O primeiro número.
    numero2 (int): O segundo número.

  Retorna:
    int: O maior número entre numero1 e numero2.
  """
  if numero1 > numero2:
    return numero1
  else:
    return numero2

# Solicita ao usuário que digite dois números
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Encontra o maior número entre os dois números digitados
maior = maior_numero(numero1, numero2)

# Imprime o maior número
print("O maior número é:", maior)
