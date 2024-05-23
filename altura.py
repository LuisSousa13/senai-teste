def peso_ideal(altura):
  """
  Calcula o peso ideal de uma pessoa com base na altura, utilizando a fórmula de Lorentz.

  Argumentos:
    altura: A altura da pessoa em metros (float).

  Retorna:
    O peso ideal da pessoa em quilogramas (float).
  """
  peso_ideal = (72.7 * altura) - 58
  return peso_ideal

# Pede a altura do usuário
altura_usuario = float(input("Digite sua altura em metros: "))

# Calcula o peso ideal
peso_ideal_usuario = peso_ideal(altura_usuario)

# Mostra o peso ideal
print(f"Seu peso ideal é de aproximadamente: {peso_ideal_usuario:.2f} kg.")
