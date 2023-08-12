# python_gerar_orcamento_pdf

## Gerar automaticamente orçamento em PDF com Python 
    Desenvolvendo as entradas de dados
    Descrição do projeto
    Total de horas estimadas Valor da hora de trabalho Prazo de entrega estimado

## Criando o cálculo do valor total estimado

Cálculo:
valor_total_estimado = int(horas_estimadas) * int(valor_hora) print(valor_total_estimado)
72003
Gerando o PDF com o orçamento
Instalando a biblioteca
!pip install fpdf
Criando um arquivo PDF
## importando a biblioteca
from fpdf import FPDF
pdf = FPDF() pdf.add_page() pdf.set_font("Arial")
In [36]:
 In [37]:
In [39]:
Inserindo os dados no PDF
## utilizando um template
pdf.image("template.png", x=0, y=0 )
## inserindo os dados do projeto
pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas) pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo_estimado) pdf.text(115, 205, str(valor_total_estimado))
Salvando o arquivo
 pdf.output("orçamento.pdf") print("Orçamento gerado com sucesso!")
Orçamento gerado com sucesso!