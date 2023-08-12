# Gerar automaticamente PDFs com Python
# Cenario: Emitir orcamento para sua empresa

## Desenvolvendo as entradas de dados
# Descricao do projeto
# Total de horas estimadas
# Valor da hora de Trabalho
# Prazo de entrega estimado

projeto = input("Digite a descricao do projeto: ")
horas_estimadas = input("Digite o total de horas estimadas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo_estimado = input("Digite o prazo estimado: ")

# Criando o Calculo do valor total estimado
# Calculo: valor total estimado = total de horas estimadas x valor da hora de trabalho

valor_total_estimado = int(horas_estimadas) * int(valor_hora)
print(valor_total_estimado)

# GERANDO O PDF COM ORCAMENTO
# Instalando a biblioteca
# !pip install fpdf

# importando a biblioteca 
from fpdf import FPDF

# Criando um arquivo PDF
pdf = FPDF()
pdf.add_page ()
pdf.set_font("Arial")

# INSERINDO OS DADOS NO PDF
# utilizando um template
pdf.image("template.png", x=0, y=0)

#inserindo os dados do projeto
pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo_estimado)
pdf.text(115, 205, str(valor_total_estimado))

# SALVANDO O ARQUIVO
pdf.output("orcamento.pdf")
print("Orcamento gerado com Sucesso!")



