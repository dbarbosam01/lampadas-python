### Cálculo de Lâmpadas para Iluminação de Cômodo
'''
Este programa calcula a quantidade de lâmpadas necessárias para iluminar um determinado
cômodo baseado em suas dimensões e na potência da lâmpada utilizada,
seguindo as diretrizes:
* **Potência necessária:** 3 watts por metro quadrado ($m^2$).
* **Capacidade física:** 1 bocal de lâmpada a cada 3 $m^2$.
'''


print("--- Cálculo de Lâmpadas Necessárias ---")
# Entrada dos dados
potencia_lampada = float(input("Digite a potência da lâmpada utilizada (em Watts): "))
largura = float(input("Digite a largura do cômodo (em metros): "))
comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

# Validação simples
if potencia_lampada <= 0 or largura <= 0 or comprimento <= 0:
  print("Erro: Todos os valores devem ser maiores que zero.")
  print("Erro: Por favor, digite valores numéricos válidos.")

else:
  # Cálculo da área e potência necessária (3W por m²)
  area = largura * comprimento
  potencia_necessaria = area * 3
  # Quantidade de lâmpadas (arredondando para cima)
  qtd_lampadas = (potencia_necessaria // potencia_lampada)
  if potencia_necessaria % potencia_lampada > 0:
    qtd_lampadas += 1
  # Exibição do resultado
  print("\n--- Resultado ---")
  print(f"Área do cômodo: {area:.2f} m²")
  print(f"Potência total necessária: {potencia_necessaria:.2f} W")
  print(f"Quantidade de lâmpadas necessárias: {qtd_lampadas}")
    